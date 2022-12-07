import sharepy
# from sharepy import connect
# from sharepy import SharePointSession

def download_sharepoint_file(conn):
    """
    This function is used to download the file placed at sharepoint
    """
    # Create header for the http request
    my_headers = {
    'accept' : 'application/json;odata=verbose',
    'content-type' : 'application/json;odata=verbose',
    'odata' : 'verbose',
    'X-RequestForceAuthentication' : 'true'
    }
    site = "https://assetmark-my.sharepoint.com/:x:/r/personal/rishi_bhadoria_assetmark_com/Documents/Documents/AM_2022/QA%20Transition/QA_Leave_Tracker_2022.xlsx"
    
    local_file_path=r'C:\Users\Paritosh.Sharma\Downloads\test_file.xlsx'
    response = conn.getfile(site,headers = my_headers,filename = local_file_path)