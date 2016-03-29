
public class Driver {

	public static void main(String[] args) {
		Encryptable Caesar = new CaesarInt();
		
		String key = "22";
		
		String eMessage = Caesar.encrypt("programming is the best", key);
		System.out.println(eMessage);
		
		String dMessage = Caesar.decrypt(eMessage, key);
		System.out.println(dMessage);
	}
}
