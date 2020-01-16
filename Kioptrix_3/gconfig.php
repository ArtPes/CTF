<?php
	error_reporting(0);
	/*
		A sample Gallarific configuration file. You should edit
		the installer details below and save this file as gconfig.php
		Do not modify anything else if you don't know what it is.
	*/

	// Installer Details -----------------------------------------------

	// Enter the full HTTP path to your Gallarific folder below,
	// such as http://www.yoursite.com/gallery
	// Do NOT include a trailing forward slash

	$GLOBALS["gallarific_path"] = "http://kioptrix3.com/gallery";

	$GLOBALS["gallarific_mysql_server"] = "localhost";
	$GLOBALS["gallarific_mysql_database"] = "gallery";
	$GLOBALS["gallarific_mysql_username"] = "root";
	$GLOBALS["gallarific_mysql_password"] = "fuckeyou";

	// Setting Details -------------------------------------------------

if(!$g_mysql_c = @mysql_connect($GLOBALS["gallarific_mysql_server"], $GLOBALS["gallarific_mysql_username"], $GLOBALS["gallarific_mysql_password"])) {
		echo("A connection to the database couldn't be established: " . mysql_error());
		die();
}else {
	if(!$g_mysql_d = @mysql_select_db($GLOBALS["gallarific_mysql_database"], $g_mysql_c)) {
		echo("The Gallarific database couldn't be opened: " . mysql_error());
		die();
	}else {
		$settings=mysql_query("select * from gallarific_settings");
		if(mysql_num_rows($settings)!=0){
			while($data=mysql_fetch_array($settings)){
				$GLOBALS["{$data['settings_name']}"]=$data['settings_value'];
			}
		}
	
	}
}

?>
