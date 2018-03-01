package com.hascode.cars;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;
import java.util.ArrayList;
import java.util.HashMap;

public class Parser{
  private String file_path;
  private HashMap<Integer, ArrayList<Ride>> rides;
  private HashMap<String, Integer> data;

  //file_path -> stringa del file recuperata da argv
  public Parser(String file_path){
    this.file_path = file_path;
  }
  public void read(){

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
