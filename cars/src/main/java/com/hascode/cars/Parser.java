package com.hascode.cars;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;
import java.util.ArrayList;
import java.util.HashMap;

public class Parser{
  private Stream<String> fileStream;
  private HashMap<Integer, ArrayList<Ride>> rides;
  private HashMap<String, Integer> data;

  public Parser(Stream<String> fileStream){
    this.fileStream = fileStream;
    this.rides = new HashMap();
    this.data = new HashMap();
  }
  private void fillData(String[] values){
    data.put("r", Integer.parseInt(values[0]));
    data.put("c", Integer.parseInt(values[1]));
    data.put("f", Integer.parseInt(values[2]));
    data.put("n", Integer.parseInt(values[3]));
    data.put("b", Integer.parseInt(values[4]));
    data.put("t", Integer.parseInt(values[5]));
  }
  public void read(){
      String dataLine = fileStream.findFirst().toString();
      this.fillData(dataLine.split(" "));

  }
  public  void parse(){
  }
  public HashMap<Integer, ArrayList<Ride>> getRides(){
    return new HashMap<Integer, ArrayList<Ride>>();
  }
  public HashMap<String, Integer> getData(){
    return new HashMap<String, Integer>();
  }
}
