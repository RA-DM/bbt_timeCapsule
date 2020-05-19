$(function(){
    allload();
    var nowpage=window.location.pathname.match(/(\w+.html)$/) [0];
    function allload(){

        var imgdownload = new createjs.LoadQueue(true);
        var idx=1;
        var timer = setInterval(function(){
            if(idx>3){
                idx=1;
            }
            var src="./images/"+idx+".png";
            idx++;
            $("#rotate").attr("src",src);
        },500)
        function handleComplete(){
            //加载完成 等其他图片放进来以后 把图片放进↓的加载列表 就打开
            $("#loading").fadeOut(800);
           clearInterval(timer);
        }

        // imgdownload.on("fileload", handleFileLoad, this);
        imgdownload.on("complete", handleComplete, this);
        imgdownload.loadManifest([
            "./images/return.png",
            "./images/地图-弹框.png",
        ]);
    imgdownload.load();
}
})