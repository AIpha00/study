const jsdom = require("jsdom");
const {JSDOM} = jsdom;

// const dom = new JSDOM(`<!DOCTYPE html><p>Hello world</p>`, {
//     url: "https://example.org/",
//     referrer: "https://example.com/",
//     contentType: "text/html",
//     userAgent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36/",
//     includeNodeLocations: true
//   }).window
var options = {
  "userAgent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
};
JSDOM.fromURL("https://www.nike.com/cn/", options).then(dom => {
  console.log(options.userAgent)
  console.log(dom.userAgent);
  dom.window.window.navigator.userAgent = "ssss"
  console.log(dom.window.window.navigator.userAgent);
  console.log(dom.window.window.document.documentURI)
});