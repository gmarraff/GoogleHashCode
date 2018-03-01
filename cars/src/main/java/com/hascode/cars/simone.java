package com.hascode.cars;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

class Rider {

}
class Simone {
    static List<Ride> retrieveRiders(Integer diag, int xM, int yM, HashMap<Integer, ArrayList<Ride>> riders, int nDiag, int k){

        ArrayList<Ride> diag1 = new ArrayList<>();
        IntStream.range(0, nDiag).forEach(
                x -> {  riders.get(x)
                        .stream()
                        .forEach(rid ->diag1.add(rid));}
        );


        ArrayList<Ride> diag2 = riders.get(diag);
        ArrayList<Ride> diag3 = riders.get(diag+1);


        return diag1
                .stream()
                .filter(r-> r.x >= xM-k && r.x <= xM+k).collect(Collectors.toList());
    }

    static void chooseNext(){

    }



    public static void main(String[] args) {
        System.out.println("cioa");
    }
}
