package com.hascode.cars;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.stream.IntStream;
import java.util.Comparator;
public class Parser{
  private ArrayList<String> fileContent;
  private MultiMap<Integer, Ride> rides;
  private HashMap<Integer, ArrayList<Ride>> orderedRides;
  private HashMap<String, Integer> data;

  public Parser(Stream<String> fileStream){
    fileContent = new ArrayList();
    fileStream.forEach(s -> fileContent.add(s));
    this.rides = new MultiMap();
    this.data = new HashMap();
    this.parse();
  }
  private void fillData(String[] values){
    this.data.put("r", Integer.parseInt(values[0]));
    this.data.put("c", Integer.parseInt(values[1]));
    this.data.put("f", Integer.parseInt(values[2]));
    this.data.put("n", Integer.parseInt(values[3]));
    this.data.put("b", Integer.parseInt(values[4]));
    this.data.put("t", Integer.parseInt(values[5]));
  }
  private void fillRides(){
    IntStream.range(0, fileContent.size()).skip(1)
    .forEach(idx -> {
      String raw_ride = fileContent.get(idx);
      String[] split_ride = raw_ride.split(" ");
      Ride ride = new Ride(idx,
                          Integer.parseInt(split_ride[0]),
                          Integer.parseInt(split_ride[1]),
                          Integer.parseInt(split_ride[2]),
                          Integer.parseInt(split_ride[3]),
                          Integer.parseInt(split_ride[4]),
                          Integer.parseInt(split_ride[5])
                          );
      Integer distance = ride.x + ride.y;
      rides.put(distance, ride);
    });
  }
  /*private void orderRides(){
    this.orderedRides = new MultiMap();
    this.rides.keySet().stream().forEach(key -> {
      this.orderedRides.put(key, rides.stream().sorted(Comparator.comparing(Ride::getX)));
    });
  }*/
  public  void parse(){
    String dataLine = this.fileContent.stream().findFirst().get();
    this.fillData(dataLine.split(" "));
    this.fillRides();
    //this.orderRides();
  }
  public MultiMap<Integer, Ride> getRides(){
    return this.rides;
  }
  public HashMap<String, Integer> getData(){
    return this.data;
  }
}
