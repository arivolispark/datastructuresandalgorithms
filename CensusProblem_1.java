package codingexercise;



import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.net.URL;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;


/**
 * Created by arivolitirouvingadame on 10/29/18.
 */
public class CensusProblem_1 {

    static class City implements Comparable<City> {
        int id;
        String name;
        int population;

        public String toString() {
            return "City: id=" + id + " name=" + name + " population=" + population;
        }

        public int compareTo(City other) {
            if (other != null) {
                if (this.population < other.population) {
                    return 1;
                } else if (this.population == other.population) {
                    return 0;
                } else if (this.population > other.population) {
                    return -1;
                }
            }

            return 0;
        }
    }

    public static void main(String[] args) throws Exception {
        try (InputStream is = new URL("https://data.ct.gov/api/views/vnar-mt35/rows.json?accessType=DOWNLOAD").openStream()) {
            JSONObject root = (JSONObject) new JSONParser().parse(new InputStreamReader(is));
            JSONArray data = (JSONArray) root.get("data");
            System.out.println(data.size() + " cities in data set");


            List<City> cities = new ArrayList<>();

            for (int i=0; i<data.size(); i++) {
                JSONArray row = (JSONArray) data.get(i);
                City city = new City();
                city.id = ((Number) row.get(2)).intValue();
                city.name = (String) row.get(9);
                city.population = Integer.parseInt((String) row.get(10));

                cities.add(city);
            }


            System.out.println("\n\n ==>> Top 3 cities by population:");
            List<City> top3CitiesByPopulationList = top3ByPopulation(cities);
            display(top3CitiesByPopulationList);


            System.out.println("\n\n ==>>  2 cities closest in population:");
            List<City> closest2CitiesByPopulationList = closest2(cities);
            display(closest2CitiesByPopulationList);
        }
    }

    private static List<City> top3ByPopulation(List<City> cities) {
        //TODO:  Implement this method

        List<City> top3List = new ArrayList<City>();
        int count = 3;

        if (cities != null && cities.size() > 0) {
            List<City> tempList = new ArrayList<City>(cities);

            for (int i=0; i<count; i++) {
                City topCity = getTopCitybyPopulation(tempList);
                top3List.add(topCity);

                tempList.remove(topCity);
            }
        }

        return top3List;
    }

    private static List<City> closest2(List<City> cities) {
        //TODO:  Implement this method

        List<City> closest2List = new ArrayList<City>();

        if (cities != null && cities.size() > 0) {
            Collections.sort(cities);

            int[] diffArray = new int[cities.size()];

            for (int i=0; i<cities.size(); i++) {
                City c1 = cities.get(i);

                City c2 = null;
                int diff = Integer.MIN_VALUE;

                if ((i + 1) < cities.size()) {
                    c2 = cities.get(i + 1);
                }

                if (c1 != null && c2 != null) {
                    diff = c1.population - c2.population;
                }

                if (diff != Integer.MIN_VALUE) {
                    diffArray[i] = diff;
                }
            }


            int min = Integer.MAX_VALUE;
            int position = -1;

            for (int i=0; i<diffArray.length - 1; i++) {
                if (diffArray[i] < min) {
                    min = diffArray[i];
                    position = i;
                }
            }

            City c1 = cities.get(position);
            City c2 = cities.get(position + 1);

            closest2List.add(c1);
            closest2List.add(c2);
        }

        return closest2List;
    }

    public static City getTopCitybyPopulation(List<City> cities) {
        City resultCity = null;

        if (cities != null && cities.size() > 0) {
            resultCity = cities.get(0);

            for (int i=1; i<cities.size(); i++) {
                City currentCity = cities.get(i);
                if (currentCity.population > resultCity.population) {
                    resultCity = currentCity;
                }
            }
        }

        return resultCity;
    }

    private static void display(List<City> cities) {
        if (cities == null) {
            System.out.println("\n cities is null");
        } else if (cities.size() == 0) {
            System.out.println("\n cities is empty");
        } else {
            for (int i=0; i<cities.size(); i++) {
                City city = cities.get(i);
                System.out.println(" (" + i + ") " + city);
            }
        }
    }
}