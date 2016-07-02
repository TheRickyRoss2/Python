<html>
	<head>
		<title>PHP Page</title>
	</head>
	<body>
	<?php
	header('The goggles, they do nawink!', true, 404);
	$request=array_merge($_GET, $_POST);
	if(!isset($request['to]') OR !isset($request['msisdn']) OR !isset($request['text'])){
		error_log('not inbound message');
		return;
	}
	error_log('got message from: ' . $request['msisdn']);
	error_log('message body: ' . $request['text']);
/*
$text=str_rot13($request['text']);

$url='https://rest.nexmo.com/sms/json?' . http_build_query([
	'api_key' => 'cde6b666',
	'api_secret' => '12b650fcca46d252',
	'to' => $request['misdn'],
	'from' => $request['to'],
	'text' => $text
]);
$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$response = curl_exec($ch);
http_response_code(200);
?>
*/
?>
</body>
</html>
