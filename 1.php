<?php
$curl = curl_init();
curl_setopt_array($curl, array(
    CURLOPT_RETURNTRANSFER => 1,
    CURLOPT_URL => 'https://ifb.vn/FacebookApi',
    CURLOPT_USERAGENT => 'Viblo Exmaple POST',
    CURLOPT_POST => 1,
    CURLOPT_SSL_VERIFYPEER => false, //Bỏ kiểm SSL
    CURLOPT_POSTFIELDS => http_build_query(array(
        'type_api'=> 'Get_Cookie_Facebook',
        'userphone'=> '0363006192',
        'api_key'=> '6u2TDS1D+pF2JTKMfCftraMDWQHshJbHmDpJIOOubxE=',
        'proxy'=> 'VN',
        'username'=> '100087238674762',
        'pwusername'=> 'Duat8aZz',
        'otp'=> '181818',
    ))
));
$resp = curl_exec($curl);

#var_dump($resp);
curl_close($curl);
$ketqua = json_decode($resp, true);
$cookie=$ketqua['cookie'];
echo $cookie."\n" ;


?>
