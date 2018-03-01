package com.hascode.cars;

import com.hashcode.cars.OutputWriter;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class Main {

    private static final String ES1 = "a_example.in";
    private static final String ES2 = "b_should_be_easy.in";
    private static final String ES3 = "c_no_hurry.in";
    private static final String ES4 = "d_metropolis.in";
    private static final String ES5 = "e_high_bonus.in";

    public static void main(String[] args) throws URISyntaxException {
        InputStreamReader resource = new InputStreamReader(Thread.currentThread().getContextClassLoader()
                .getResourceAsStream(ES1));
        BufferedReader bufferedInputStream = new BufferedReader(resource);
        Parser parser = new Parser(bufferedInputStream.lines());
        Map<String, Integer> data = parser.getData();
        data.get("t");
    }

}
