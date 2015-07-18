// opinion_date.js: extract date for cases from GS
if (window == top) {
  chrome.extension.onRequest.addListener(function(req, sender, sendResponse) {
    sendResponse(findDate());
  });
}

// Search the text nodes for a date in a title of a Google Scholar case
var findDate = function() {
    var re = /([0-9]{4})\s\-\sGoogle Scholar$/g;
    var title = document.title;
    //var done = false;

    var date = null;

    var result = re.exec(title);
    if (result) {
        date = result[1]
    }
    console.log("The date of the case is: " + date);
    return date
}
