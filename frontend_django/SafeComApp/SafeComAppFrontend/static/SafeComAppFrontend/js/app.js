if("serviceWorker" in navigator){
   navigator.serviceWorker
    .register("/sw.js")
    .then(reg => console.log("service worker registred", reg))
    .catch(err => console.log("services worker no registed",err))
}