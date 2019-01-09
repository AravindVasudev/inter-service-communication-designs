import java.rmi.Naming; 
import java.rmi.RemoteException; 
import java.rmi.server.UnicastRemoteObject;

public class Server extends UnicastRemoteObject implements DemoInterface {
    public Server() throws RemoteException {}

    public String sayHello() { return "Hello world!"; }

    public static void main(String[] args) throws Exception {
        Naming.rebind("//localhost/Server", new Server());
    }
}