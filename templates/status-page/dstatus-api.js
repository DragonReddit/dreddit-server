function httpGet(url, objectIdToChange) {
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open('GET', url, true);
    xmlHttp.setRequestHeader('X-Requested-With', 'XMLHttpRequest'); 
    xmlHttp.setRequestHeader('Access-Control-Allow-Origin', '*');
    xmlHttp.send(null);

    if (xmlHttp.status == 200) {
        document.getElementById(objectIdToChange).innerText = 'Working';
        document.getElementById(objectIdToChange).className = 'dstatusDone';
        return xmlHttp;
    }
    else {
        console.log(xmlHttp.response)
        document.getElementById(objectIdToChange).innerText = 'Error';
        document.getElementById(objectIdToChange).className = 'dstatusError';
        return "Failed";
    }
}