`timescale 1ns/1ps

module rgb2grayscale_tb ();
    parameter INT_WIDTH = 8;
    parameter FP_WIDTH = 16;
    parameter Clock_Cycle = 80;
    reg [INT_WIDTH-1:0] RED,
              BLUE,
              GREEN;
    reg CLK, 
        DIN_VALID,
        RST_NEG;
    wire [INT_WIDTH-1:0] GRAYSCALE;
    wire DOUT_VALID;
    
    reg [INT_WIDTH-1:0]  mem [0:((1<<20)-1)];
    reg [12:0] shape [0:3];

    integer i,
            write_data,
	        temp;

    initial begin
        CLK <= 1'b0;
        DIN_VALID <= 1'b1;
        RST_NEG <=1;
        i <= 0;
        #(Clock_Cycle/4)
        //Modify path in this 
        //$readmemb("/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/bin_in.txt", mem);
        $readmemb("/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/bin_in_temp.txt", mem);
	    
         //Modify path in this 
        //$readmemb("/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/Dimensions.txt", shape);
        $readmemb("/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Dimensions.txt", shape);
         
         //Modify path in this 
        //write_data = $fopen("/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/bin_out.txt");
        write_data = $fopen("/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/bin_out_temp.txt");
        temp = shape[0] * shape[1];
        while (i < temp)
        begin
            if (!RST_NEG)
            begin
                i <= 0; 
            end
            else 
            begin
                if (DIN_VALID)
                begin
                    RED   <= mem[(temp * 0) + i];
                    GREEN <= mem[(temp * 1) + i];
                    BLUE  <= mem[(temp * 2) + i];
                    i <= i + 1;
                    #(Clock_Cycle)
                    if(i > 3)
                        $fdisplay(write_data, "%b", GRAYSCALE); 
                end 
                else
                begin
                    RED <= 8'bz;
                    GREEN <= 8'bz;
                    BLUE <= 8'bz;
                end
            end
        end  
        for (i=0; i < 3; i=i+1)
        begin
            $fdisplay(write_data, "%b", GRAYSCALE);
        end
        $fclose(write_data);
        #(Clock_Cycle*4) $finish;
    end

    always @(CLK)
        #(Clock_Cycle/2) CLK <= ~CLK;

    rgb2grayscale dut (
        .grayscale  (GRAYSCALE),
        .dout_valid (DOUT_VALID), 
        .R          (RED), 
        .G          (GREEN), 
        .B          (BLUE), 
        .clk        (CLK), 
        .din_valid  (DIN_VALID),
        .rst_neg    (RST_NEG)
    );
endmodule
