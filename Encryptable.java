public interface Encryptable {
	
	public String encrypt(String message, String key);
	
	public String decrypt(String message, String key);
	
}
