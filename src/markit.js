//this code doesn't do much yet- out of time
//the intent is to write the function to highlight the USC citations on a page, given an array of citations

<script>
function markIt(paraAsString, arrayOfCitations) {

	paragraph = paraAsString;
	citeList = Array();
	citeList = arrayOfCitations;
	citeListCounter = 0;

	//for (citeListCounter;arrayOfCitations.length;citeListCounter++) {

	posCite = paraAsString.search(citeList[citeListCounter]); //this should give the position of the first USC citation
	//citeLength = length.citeList[citeListCounter];
	//}
	//alert(posCite);
	//alert(paragraph);
	//alert(citeList);
	//alert(posCite);

	output = [paragraph.slice(0, posCite), "<span style='font:blue;'>", paragraph.slice(posCite),"</span>"].join('');
	alert(output);
	document.getElementById("targetParagraph").innerHTML = output;

;}
</script>
