import java.rmi.*;

public interface DemoInterface extends java.rmi.Remote {
	String sayHello() throws RemoteException;
}