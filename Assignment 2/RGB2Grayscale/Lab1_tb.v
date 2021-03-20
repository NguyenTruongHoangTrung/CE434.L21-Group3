`timescale 1ns/1ps

module Lab1_tb ();
    reg [7:0] RED,
              BLUE,
              GREEN;
    reg CLK, 
        RESET;
    wire [7:0] GRAYSCALE;
    
    reg [7:0] mem [0:((1<<20)-1)];
    reg [12:0] res [0:3];

    integer i,
            write_data,
	    temp;

    initial begin
        CLK <= 0;
        RESET <= 1;
        #120
        
        RESET <= 0;
        $readmemb("/home/trungnguyen/Documents/CE434-Embedded Image Processing on FPGA/Labs/Assignment_2/RGB2Grayscale/bin.txt", mem);
	    $readmemb("/home/trungnguyen/Documents/CE434-Embedded Image Processing on FPGA/Labs/Assignment_2/Dimensions.txt", res);
        write_data = $fopen("/home/trungnguyen/Documents/CE434-Embedded Image Processing on FPGA/Labs/Assignment_2/RGB2Grayscale/write_mem.txt");
        temp = res[0] * res[1];
        for (i=0; i < temp; i=i+1)
        begin
            
            RED   = mem[(temp * 0) + i];
            GREEN = mem[(temp * 1) + i];
            BLUE  = mem[(temp * 2) + i];
            #80

            $fdisplay(write_data, "%b", GRAYSCALE);
        end

        $fclose(write_data);
        $finish;
    end

    always @(CLK)
        #40 CLK <= ~CLK;

    rgb2grayscale dut 
        (.grayscale(GRAYSCALE), 
        .R(RED), 
        .G(GREEN), 
        .B(BLUE), 
        .clk(CLK), 
        .rst(RESET));
endmodule