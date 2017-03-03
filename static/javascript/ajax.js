function loadXMLDocByGet(url,cfunc,xmlhttp)                                               //AJAX-----使用GET方式
{    
    xmlhttp.onreadystatechange=cfunc;
    xmlhttp.open("GET",url,true);
    xmlhttp.send();
}
function loadXMLDocByPost(send_content,url,cfunc,xmlhttp)                   //AJAX-----使用POST方式
{
    xmlhttp.onreadystatechange=cfunc;
    xmlhttp.open("POST",url,true);
    xmlhttp.setRequestHeader("Content-type","application/json");
    xmlhttp.send(send_content);
}
