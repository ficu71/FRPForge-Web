package com.example.wificrackconnector;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.net.wifi.WifiManager;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        WifiManager wifiManager = (WifiManager) getSystemService(WIFI_SERVICE);
        TextView statusText = findViewById(R.id.statusText);

        if (wifiManager != null && wifiManager.isWifiEnabled()) {
            statusText.setText("WiFi Manager Active\nReady for operations");
        } else {
            statusText.setText("Enable WiFi to proceed");
        }
    }
}
