// Michael Chunko
// Mr. Gill
// CS4
// 2018

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

public class Preprocessing {
    // Takes a .txt file and converts it to a format usable by the language
    // detection program
    // The expected format of the unprocessed .txt file is the format provided
    // by The Leipzig Corpora Collection using the *-sentences.txt from a corpus
    // Parameters:
    //  inputPath: the filepath of the file to be read from
    //  outputPath: the filepath of the file to write to
    //  languageCode: The language code of the input language. Leave it as "" if this it to be a test file
    public static void prepareData(String inputPath, String outputPath, String languageCode) {
        // The new version of the document contents containing cleaned-up data
        ArrayList<String> newParts = new ArrayList<String>();

        // Reading in and cleaning up the input
        try {
            FileReader fileReader = new FileReader(inputPath);
            BufferedReader bufferedReader = new BufferedReader(fileReader);
            String line = bufferedReader.readLine();

            while (line != null) {
                String[] parts = line.split(" ");
                for (int i = 0; i < parts.length; i++) {
                    boolean isLowerCase = true;
                    for (int j = 0; j < parts[i].length() && isLowerCase; j++) {
                        char currentChar = parts[i].charAt(j);

                        // Replaces non-standard characters with their English 26-letter alphabet equivalent
                        String replacement = "";
                        switch (currentChar) {
                            //Uppercase version of characters
                            case 192: //À
                            case 193: //Á
                            case 194: //Â
                            case 195: //Ã
                                replacement = "a";
                                break;
                            case 196: //Ä
                                replacement = "ae";
                                break;
                            case 197: //Å
                                replacement = "a";
                                break;
                            case 198: //Æ
                                replacement = "e";
                                break;
                            case 199: //Ç
                                replacement = "c";
                                break;
                            case 200: //È
                            case 201: //É
                            case 202: //Ê
                            case 203: //Ë
                                replacement = "e";
                                break;
                            case 204: //Ì
                            case 205: //Í
                            case 206: //Î
                                replacement = "i";
                                break;
                            case 207: //Ï
                                replacement = "ie";
                                break;
                            case 208: //Ð
                                replacement = "th";
                                break;
                            case 209: //Ñ
                                replacement = "n";
                                break;
                            case 210: //Ò
                            case 211: //Ó
                            case 212: //Ô
                            case 213: //Õ
                                replacement = "o";
                                break;
                            case 214: //Ö
                            case 216: //Ø
                                replacement = "oe";
                                break;
                            case 217: //Ù
                            case 218: //Ú
                            case 219: //Û
                                replacement = "u";
                                break;
                            case 220: //Ü
                                replacement = "ue";
                                break;
                            case 221: //Ý
                                replacement = "y";
                                break;
                            case 222: //Þ
                                replacement = "th";
                                break;
                            //Lowercase version of characters
                            case 223: //ß
                                replacement = "ss";
                                break;
                            case 224: //à
                            case 225: //á
                            case 226: //â
                            case 227: //ã
                                replacement = "a";
                                break;
                            case 228: //ä
                                replacement = "ae";
                                break;
                            case 229: //å
                                replacement = "a";
                                break;
                            case 230: //æ
                                replacement = "e";
                                break;
                            case 231: //ç
                                replacement = "c";
                                break;
                            case 232: //è
                            case 233: //é
                            case 234: //ê
                            case 235: //ë
                                replacement = "e";
                                break;
                            case 236: //ì
                            case 237: //í
                            case 238: //î
                                replacement = "i";
                                break;
                            case 239: //ï
                                replacement = "ie";
                                break;
                            case 240: //ð
                                replacement = "th";
                                break;
                            case 241: //ñ
                                replacement = "n";
                                break;
                            case 242: //ò
                            case 243: //ó
                            case 244: //ô
                            case 245: //õ
                                replacement = "o";
                                break;
                            case 246: //ö
                            case 248: //ø
                                replacement = "oe";
                                break;
                            case 249: //ù
                            case 250: //ú
                            case 251: //û
                                replacement = "u";
                                break;
                            case 252: //ü
                                replacement = "ue";
                                break;
                            case 253: //ý
                                replacement = "y";
                                break;
                            case 254: //þ
                                replacement = "th";
                                break;
                            case 255: //ÿ
                                replacement = "y";
                                break;
                            case 352: //Š
                                replacement = "sh";
                                break;
                            case 353: //š
                                replacement = "sh";
                                break;
                            case 381: //Ž
                                replacement = "zh";
                                break;
                            case 382: //ž
                                replacement = "zh";
                                break;
                            case 268: //Č
                                replacement = "ch";
                                break;
                            case 269: //č
                                replacement = "ch";
                                break;
                            case 280: //Ę
                                replacement = "ch";
                                break;
                            case 281: //ę
                                replacement = "ch";
                                break;
                        }

                        // If a non-standard character was found, replaces it with its standard equivalent
                        if (!replacement.equals("")) {
                            if (j == parts[i].length() - 1) {
                                parts[i] = parts[i].substring(0, j) + replacement;
                            } else {
                                parts[i] = parts[i].substring(0, j) + replacement + parts[i].substring(j + 1);
                            }
                            currentChar = parts[i].charAt(j);
                        }

                        // Prevents words with punctuation, or uppercase words such as
                        // acronyms from being used
                        // Only ignores the first character in German so that nouns can be used
                        if (!(currentChar >= 97 && currentChar <= 122)) {
                            //if(languageCode != "de" || j != 0)
                            //{
                            //    isLowerCase = false;
                            //}
                            if (languageCode.equals("de") && j == 0 && currentChar >= 65 && currentChar <= 90) {
                                parts[i] = parts[i].substring(0, j) + Character.toLowerCase(currentChar) +
                                        parts[i].substring(j + 1);
                            } else
                                isLowerCase = false;
                        }

                    } // End character for loop

                    // Prevents words with punctuation, or uppercase words such as
                    // names, places, or acronyms from being used
                    // Prevents incredibly brief words like "I" or long words
                    if (isLowerCase && parts[i].length() > 1 && parts[i].length() <= 16)
                        newParts.add(parts[i]);
                } // End line parts for loop
                line = bufferedReader.readLine();
            } // End while loops to get next line

            bufferedReader.close();
        } // End input loop
        catch (FileNotFoundException ex) {
            System.out.println("Unable to open file '" + inputPath + "'");
        } catch (IOException ex) {
            System.out.println("Error reading file '" + inputPath + "'");
        }

        // Printing the contents of newParts to a text document
        try {
            BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(outputPath));

            for (int i = 0; i < newParts.size(); i++) {
                for (int j = 0; j < 16; j++) {
                    if (j == 0)
                        bufferedWriter.append("" + (int) (newParts.get(i).charAt(j) - '`'));
                    else {
                        if (j < newParts.get(i).length())
                            bufferedWriter.append("," + (int) (newParts.get(i).charAt(j) - '`'));
                        else
                            bufferedWriter.append(",0");
                    }
                }

                bufferedWriter.append("," + languageCode);

                bufferedWriter.append("\n");

                System.out.println(newParts.get(i));

            }

            bufferedWriter.close();
        } catch (FileNotFoundException ex) {
            System.out.println("Unable to open file '" + outputPath + "'");
        } catch (IOException ex) {
            System.out.println("Error reading file '" + outputPath + "'");
        } // End output loop
    }
}
