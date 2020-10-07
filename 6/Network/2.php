<?php
function isMobile(){
	return preg_match("/(android|avantgo|blackberry|bolt|boost|cricket|docomo|fone|hiptop|mini|mobi|palm|phone|pie|tablet|up\.browser|up\.link|webos|wos)/i", $_SERVER["HTTP_USER_AGENT"]);
}
	
if (isMobile()){
	echo "<h1>Yes!</h1> You are on a mobile device.";
} else {
	echo "<h1>No!</h1>You are not on a mobile device.";
}
?>