// Copyright (c) 2011 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// The background page is asking us to find an address on the page.
if (window == top) {
  chrome.extension.onRequest.addListener(function(req, sender, sendResponse) {
    sendResponse(findDate());
  });
}

// Search the text nodes for a U.S.C. citation
var findDate = function() {
    var re = /([0-9]{4})\s\-\sGoogle Scholar$/g;
    var title = document.title;
    //var done = false;

    var dates = Array();

        var result = re.exec(title);
            if (result) {
                dates.push(result[1])
                }
        //var match = title.match(re);
        //if (match) {
          //  dates.push(match);
        //}
    
    console.log(dates[0])
    console.log(dates)
    return dates;
    
}
