
/**
 * Write a description of class IsItTheFlag here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class IsItTheFlag {
    
    public static boolean isFlag(String str) {
        return str.hashCode() == 1471587914 && str.toLowerCase().hashCode() == 1472541258;
    }
    
    public static void main(String[] args)   {
        String available = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
        String flag = "aaaaaa";
        for(int a=0;a<available.length();a++) {
            for(int b=0;b<available.length();b++)   {
                for(int c=0;c<available.length();c++)   {
                    for(int d=0;d<available.length();d++)   {
                        for(int e=0;e<available.length();e++)   {
                            for(int f=0;f<available.length();f++)   {
                                flag = Character.toString(available.charAt(a)) + Character.toString(available.charAt(b)) + Character.toString(available.charAt(c)) + Character.toString(available.charAt(d)) + Character.toString(available.charAt(e)) + Character.toString(available.charAt(f));
                                if (d == 3 && e == 3) {
                                    System.out.println(flag);
                                }
                                if (isFlag(flag))   {
                                    System.out.println("YES");
                                    System.out.println(flag);
                                    System.exit(0);
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
