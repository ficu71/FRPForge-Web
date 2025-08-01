using System;
using System.Net.NetworkInformation;

namespace WifiCCrackConnector
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("=== WiFi Crack Connector ===");
            Console.WriteLine("Scanning network interfaces...\n");
            
            foreach (NetworkInterface nic in NetworkInterface.GetAllNetworkInterfaces())
            {
                if (nic.NetworkInterfaceType == NetworkInterfaceType.Wireless80211)
                {
                    Console.WriteLine($"Found WiFi adapter: {nic.Name}");
                    Console.WriteLine($"Status: {nic.OperationalStatus}\n");
                }
            }
            
            Console.WriteLine("Press ENTER to exit");
            Console.ReadLine();
        }
    }
}
