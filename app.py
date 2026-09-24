import json
import requests
import streamlit as st

st.set_page_config(
    page_title="Agentic RAG n8n Deployer", page_icon="🤖", layout="wide"
)

st.title("🤖 Deploy 'Agentic RAG Knowledge Assistant' to n8n")

# --- Configuration Sidebar ---
with st.sidebar:
    st.header("1. n8n Instance Details")
    n8n_url = st.text_input("n8n Base URL", placeholder="https://n8n.yourdomain.com").rstrip("/")
    api_key = st.text_input("n8n API Key", type="password")

    st.markdown("---")
    st.header("2. Google Gemini Credentials")
    st.caption("Enter the Credential ID for your Google Gemini account on the target n8n instance.")
    gemini_credential_id = st.text_input("Gemini Credential ID", value="i3DZdkrZnTFOmjqe")

headers = {
    "X-N8N-API-KEY": api_key,
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# --- File Loader ---
st.subheader("Upload Workflow JSON")
uploaded_file = st.file_uploader("Select your workflow JSON file", type=["json"])

if uploaded_file:
    raw_data = json.load(uploaded_file)
    st.success(f"Loaded workflow: **{raw_data.get('name', 'Unnamed')}**")

    # Workflow summary
    nodes = raw_data.get("nodes", [])
    st.info(f"Detected **{len(nodes)} nodes** across File Ingestion, URL Ingestion, and RAG Chat.")

    if st.button("🚀 Deploy & Activate to n8n", type="primary"):
        if not n8n_url or not api_key:
            st.error("Please fill in both the n8n Base URL and API Key in the sidebar.")
        else:
            # 1. Update Credential IDs to match target instance
            if gemini_credential_id:
                for node in nodes:
                    if "credentials" in node and "googlePalmApi" in node["credentials"]:
                        node["credentials"]["googlePalmApi"]["id"] = gemini_credential_id

            # 2. Build payload (omit server-managed attributes like id, versionId, meta)
            payload = {
                "name": raw_data.get("name", "Agentic RAG Knowledge Assistant"),
                "nodes": nodes,
                "connections": raw_data.get("connections", {}),
                "settings": raw_data.get("settings", {}),
            }

            deploy_endpoint = f"{n8n_url}/api/v1/workflows"

            with st.spinner("Deploying workflow to n8n..."):
                try:
                    response = requests.post(deploy_endpoint, headers=headers, json=payload)

                    if response.status_code in (200, 201):
                        created_workflow = response.json()
                        workflow_id = created_workflow.get("id")
                        st.success(f"✅ Successfully created workflow! **ID: `{workflow_id}`**")

                        # 3. Activate the workflow
                        activate_endpoint = f"{n8n_url}/api/v1/workflows/{workflow_id}/activate"
                        act_response = requests.post(activate_endpoint, headers=headers)

                        if act_response.status_code in (200, 204):
                            st.success("⚡ Workflow activated and live in production!")
                        else:
                            st.warning("⚠️ Workflow deployed, but activation failed. Check credentials inside n8n.")

                        # 4. Display Direct Access URLs
                        st.markdown("### 🔗 Production Webhook Endpoints")
                        for node in nodes:
                            if node.get("type") == "n8n-nodes-base.formTrigger":
                                webhook_path = node.get("webhookId")
                                st.write(f"**Document Ingestion Form:** `{n8n_url}/form/{webhook_path}`")
                            elif node.get("type") == "@n8n/n8n-nodes-langchain.chatTrigger":
                                webhook_path = node.get("webhookId")
                                st.write(f"**Chat Interface Webhook:** `{n8n_url}/webhook/{webhook_path}/chat`")

                    else:
                        st.error(f"Deployment failed ({response.status_code}): {response.text}")

                except requests.exceptions.RequestException as e:
                    st.error(f"Network error connecting to n8n instance: {e}")
