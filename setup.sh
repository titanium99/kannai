#! /bin/bash
echo "--- Line Bot app setup. ---"
read -sp "set your channnel access token:" LINE_CHANNEL_ACCESS_TOKEN
export LINE_CHANNEL_ACCESS_TOKEN
echo $LINE_CHANNEL_ACCESS_TOKEN

read -sp "set your channnel access token:" LINE_CHANNEL_SECRET
export LINE_CHANNEL_SECRET
echo ""
echo "Finish Set!"