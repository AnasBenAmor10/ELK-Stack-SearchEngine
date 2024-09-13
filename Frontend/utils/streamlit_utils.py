import streamlit as st
import requests
def check_server(client):
    if client.ping() == False:
        st.toast("Elastic Search Server Is Not Running!")
        
def display_results(client,query,searchtype):
    check_server(client)
    getreq = {
            searchtype: {"tags":query}
    }
    results = client.search(index="flickrphotos", query=getreq) 
    # print(results)
    cols = st.columns(2)
    col_heights = [0, 0]
    displayed_images = 0
    for hit in results["hits"]['hits']:
        if displayed_images >= 16:
            break
        image_data = hit["_source"]
        image= "http://farm"+image_data['flickr_farm']+".staticflickr.com/"+image_data['flickr_server']+"/"+image_data["id"]+"_"+image_data['flickr_secret']+".jpg"
        col_id = 0 if col_heights[0] <= col_heights[1] else 1
        with st.spinner("Loading Image"):
            response = requests.get(image)
            if response.status_code == 200:
                cols[col_id].image(image)
                col_heights[col_id] += 1
                displayed_images += 1        