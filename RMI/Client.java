import java.rmi.Naming; 
import java.rmi.RemoteException;

public class Client {
    public static void main(String[] args) throws Exception {
        DemoInterface demo = (DemoInterface) Naming.lookup("//localhost/Server");
        System.out.println(demo.sayHello());
    }
}