// usc_content.js: extracts out U.S.C. site in Chromium

if (window == top) {
  chrome.extension.onRequest.addListener(function(req, sender, sendResponse) {
    sendResponse(findCites());
  });
}

// Search the text nodes for a U.S.C. citation
var findCites = function() {
    // not handling 28 U.S.C. § 2244(d)(1)
    // parenthetical subsections
    // there are sections with an alphanumeric
    var re = /(\d+)\s*U\.S\.C\.[ §]*([0-9]+(?:[a-z]{2})?)/g;
    
    var node = document.body;
    var cites = Array();

    for (var i = 0; i < node.childNodes.length; ++i) {
        var child = node.childNodes[i];
        var matches = child.textContent.match(re);
        if (matches) {
            for	(index = 0; index < matches.length; index++) {
                console.log("saw: " + matches[index])
                cites.push(matches[index]);
            }
        }
    }
    console.log("cites")
    console.log("saw " + cites.length + " citations.")
    console.log(cites)
    return cites;
}
