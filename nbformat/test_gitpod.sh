FOLDER=$(echo $GITPOD_WORKSPACE_CONTEXT | jq -r '.normalizedContextURL' | awk -F'/' '{print $NF}')
echo $FOLDER
