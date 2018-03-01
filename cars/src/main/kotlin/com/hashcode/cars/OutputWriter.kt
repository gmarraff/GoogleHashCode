package com.hashcode.cars

import java.io.File
import java.io.PrintWriter

class OutputWriter {

    fun write(fileName: String, cars: List<Int>, rides: List<List<Int>>) {
        val file = File(fileName)
        file.createNewFile()
        val outputStream = PrintWriter(file)
        cars.zip(rides)
                .filter { it.second.isNotEmpty() }
                .forEach({
                    outputStream.print(it.first)
                    outputStream.print(" ")
                    it.second.forEach {
                        outputStream.print(it)
                        outputStream.print(" ")
                    }
                    outputStream.println()
                })
        outputStream.close()
    }

}