/*import java.util.Random;
public class prgn{

     public static void main(String []args){
        long multiplier = 0x5DEECE66DL;
        long addend = 0xBL;
        long mask = (1L << 48) - 1;
        Random random = new Random();
        long v1 = random.nextInt();
        long v2 = random.nextInt();
        //v1 = -2069001995;
        //v2 = -1997362081;
        for (int i = 0; i < 65536; i++) {
            long seed = v1 * 65536 + i;
            if ((((seed * multiplier + addend) & mask) >>> 16) == v2) {
                System.out.println("Seed found: " + seed);
                break;
            }
        }
     }
}*/

import java.util.Random;

public class prgn {
    // implemented after https://docs.oracle.com/javase/7/docs/api/java/util/Random.html
    public static int next(long seed) {
        int bits=32;
        long seed2 = (seed * 0x5DEECE66DL + 0xBL) & ((1L << 48) - 1);
        return (int)(seed2 >>> (48 - bits));
    }

    public static void main(String[] args) {
        System.out.println("Starting");
        long i1 = -2069001995L;
        long i2 = -1997362081L;
        long seed =0;
        for (int i = 0; i < 65536; i++) {
            seed = i1 *65536 + i;
            if (next(seed) == i2) {
                System.out.println("Seed found: " + seed);
               break;
            }
        }
        Random random = new Random((seed ^ 0x5DEECE66DL) & ((1L << 48) - 1));
        int o1 = random.nextInt();
        int o2 = random.nextInt();
        System.out.println("So we have that nextInt is: "+o1+" and the third one is: "+o2+" with seed: "+seed);

    }
}