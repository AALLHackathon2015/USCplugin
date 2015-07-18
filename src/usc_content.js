// Copyright (c) 2011 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// The background page is asking us to find an address on the page.
if (window == top) {
  chrome.extension.onRequest.addListener(function(req, sender, sendResponse) {
    sendResponse(findCites());
  });
}

// Search the text nodes for a U.S.C. citation
var findCites = function() {
    var re = /(\d+)\s*U\.S\.C\.[ §]*([0-9]+(?:[a-z]{2})?)/mg;
    var node = document.body;
    var done = false;

    var cites = Array();

    for (var i = 0; i < node.childNodes.length; ++i) {
        var child = node.childNodes[i];
        var match = child.textContent.match(re);
        if (match) {
            cites.push(match);
        }
    }
    console.log(cites[0])
    console.log(cites)
    return cites;
    
}
