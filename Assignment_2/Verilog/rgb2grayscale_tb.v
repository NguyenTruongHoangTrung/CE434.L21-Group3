// // `timescale 1ns/1ps

// // module rgb2grayscale_tb ();
// //     parameter INT_WIDTH = 8;
// //     parameter FP_WIDTH = 16;
// //     parameter Clock_Cycle = 40;
// //     reg [INT_WIDTH-1:0] RED,
// //               BLUE,
// //               GREEN;
// //     reg CLK, 
// //         DIN_VALID,
// //         RST_NEG;
// //     wire [INT_WIDTH-1:0] GRAYSCALE;
// //     wire DOUT_VALID;
    
// //     reg [INT_WIDTH-1:0]  mem [0:((1<<20)-1)];
// //     reg [12:0] shape [0:3];

// //     integer i, k, test_rst_signal,
// //             write_data,
// // 	        temp;

// //     initial begin
// //         CLK <= 1'b0;
// //         DIN_VALID <= 1'b1;
// //         RST_NEG <=1;
// //         i = 0;
// //         test_rst_signal = 0;
// //         #(Clock_Cycle/2)
// //         //Modify path in this 
// //         //$readmemb("/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/bin_in.txt", mem);
// //         $readmemb("/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/bin_in.txt", mem);
	    
// //          //Modify path in this 
// //         //$readmemb("/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/Dimensions.txt", shape);
// //         $readmemb("/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Dimensions.txt", shape);
         
// //          //Modify path in this 
// //         //write_data = $fopen("/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/bin_out.txt");
// //         write_data = $fopen("/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/bin_out.txt");
// //         temp = shape[0] * shape[1];
// //         // for (i=0; i < temp; i=i+1)
// //         // begin
// //         //     RED   = mem[(temp * 0) + i];
// //         //     GREEN = mem[(temp * 1) + i];
// //         //     BLUE  = mem[(temp * 2) + i];
// // 	    //     #80
// //         //     if(i > 2)
// //         //         $fdisplay(write_data, "%b", GRAYSCALE);
// //         // end
// //         // for (i=0; i < 3; i=i+1)
// //         // begin
// //         //     $fdisplay(write_data, "%b", GRAYSCALE);
// //         // end
// //         while (i < temp)
// //         begin
// //             // //Test function of Reset Signal
// //             // if ((i == 10) && (test_rst_signal == 0)) 
// //             // begin
// //             //     RST_NEG <= 0;
// //             //     test_rst_signal <= 1;
// //             // end
// //             // //--------------------------
// //             //Test function of DIN_VALID signal
// //             if (i == 5)// && (test_DIN_VALID_signal == 0)) 
// //             begin
// //                 DIN_VALID <= 0;
// //                 //test_DIN_VALID_signal <= 1;
// //             end
// //             //--------------------------
// //             if (!RST_NEG)
// //             begin
// //                 i <= 0;
// //                 //Test function of Reset Signal
// //                 // #(Clock_Cycle/2) 
// //                 // RST_NEG <= 1; 
// //                 //------------------------------       
// //             end
// //             else 
// //             begin
// //                 if (DIN_VALID)
// //                 begin
// //                     RED   = mem[(temp * 0) + i];
// //                     GREEN = mem[(temp * 1) + i];
// //                     BLUE  = mem[(temp * 2) + i];
// //                     i = i + 1;
// //                     #(Clock_Cycle*2)
// //                     if(i > 2)
// //                         $fdisplay(write_data, "%b", GRAYSCALE); 
// //                 end 
// //                 else
// //                 begin
// //                     RED <= 8'bz;
// //                     GREEN <= 8'bz;
// //                     BLUE <= 8'bz;
// //                     //Test function of DIN_VALID
// //                     #(Clock_Cycle*1)
// //                     DIN_VALID <= 1;
// //                     //---------------------------
// //                 end
// //             end
// //         end  
// //         for (k=0; k < 3; k=i+1)
// //         begin
// //             $fdisplay(write_data, "%b", GRAYSCALE);
// //         end
// //         $fclose(write_data);
// //         #500 $finish;
// //     end

// //     always @(CLK)
// //         #(Clock_Cycle/2) CLK <= ~CLK;
// //     // always @(RST_NEG)
// //     //     begin
// //     //         #(Clock_Cycle*30) RST_NEG <= 0;
// //     //         #(Clock_Cycle/2) RST_NEG <= 1; 
// //     //     end
// //     // always @(DIN_VALID)
// //     // begin
// //     //     #(Clock_Cycle*10) DIN_VALID <= ~DIN_VALID;
// //     //     #(Clock_Cycle) DIN_VALID <= ~DIN_VALID;
// //     // end

// //     rgb2grayscale dut (
// //         .grayscale  (GRAYSCALE),
// //         .dout_valid (DOUT_VALID), 
// //         .R          (RED), 
// //         .G          (GREEN), 
// //         .B          (BLUE), 
// //         .clk        (CLK), 
// //         .din_valid  (DIN_VALID),
// //         .rst_neg    (RST_NEG)
// //     );
// // endmodule
// //---------------------------------------------------------------------------------------------
// `timescale 1ns/1ps

// module rgb2grayscale_tb ();
//     parameter INT_WIDTH = 8;
//     parameter FP_WIDTH = 16;
//     reg [INT_WIDTH-1:0] RED,
//               BLUE,
//               GREEN;
//     reg CLK, 
//         DIN_VALID,
//         RST_NEG;
//     wire [INT_WIDTH-1:0] GRAYSCALE;
//     wire DOUT_VALID;
    
//     reg [INT_WIDTH-1:0]  mem [0:((1<<25)-1)];
//     reg [12:0] shape [0:3];

//     integer i, k, test_rst_signal,m
//             write_data,
// 	        temp;

//     initial begin
//         CLK <= 1'b0;
//         DIN_VALID <= 1'b1;
//         begin
//             #20
//             //Modify path in this 
//             //$readmemb("/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/bin_in.txt", mem);
//             $readmemb("/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Bin_In/Bin_In_Result.txt", mem);
            
//             //Modify path in this 
//             //$readmemb("/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/Dimensions.txt", shape);
//             $readmemb("/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Dimensions.txt", shape);
            
//             //Modify path in this 
//             //write_data = $fopen("/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/bin_out.txt");
//             write_data = $fopen("/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/bin_out.txt");
//             temp = shape[0] * shape[1] * 83;
//             for (i=0; i < temp; i=i+1)
//             begin
                
//                 RED   = mem[(temp * 0) + i];
//                 GREEN = mem[(temp * 1) + i];
//                 BLUE  = mem[(temp * 2) + i];
//                 #80
//                 if(RED == 8'bxxxxxxxx || GREEN == 8'bxxxxxxxx || BLUE == 8'bxxxxxxxx)
//                 begin
//                     RED   = 8'd0;
//                     GREEN = 8'd0;
//                     BLUE  = 8'd0;
//                     DIN_VALID <= 1'b0;
//                 end    
//                 else
//                     DIN_VALID <= 1'b1;
                
//                 if(i > 2)
//                     $fdisplay(write_data, "%b", GRAYSCALE);
//             end
//             for (i=0; i < 3; i=i+1)
//             begin
//                 $fdisplay(write_data, "%b", GRAYSCALE);
//             end

//             $fclose(write_data);
//             end
//         #500 $finish;
//     end

//     always @(CLK)
//         #40 CLK <= ~CLK;

//     rgb2grayscale dut (
//         .grayscale  (GRAYSCALE),
//         .dout_valid (DOUT_VALID), 
//         .R          (RED), 
//         .G          (GREEN), 
//         .B          (BLUE), 
//         .clk        (CLK), 
//         .din_valid  (DIN_VALID)
//     );
// endmodule

`timescale 1ns/1ps

module rgb2grayscale_tb ();
    parameter INT_WIDTH = 8;
    parameter FP_WIDTH = 16;
    reg [INT_WIDTH-1:0] RED,
              BLUE,
              GREEN;
    reg CLK, 
        DIN_VALID;
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
        #20
        //Modify path in this 
        //$readmemb("/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/bin_in.txt", mem);
        $readmemb("/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/bin_in_temp.txt", mem);
        //$readmemb("/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/Dimensions.txt", shape);
        $readmemb("/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/Dimensions.txt", shape);
        
        //Modify path in this 
        //write_data = $fopen("/home/trungnguyen/Documents/CE434_Embedded_Image_Processing_on_FPGAs/Labs/Assignment_2/Output/bin_out.txt");
        write_data = $fopen("/home/viet/Documents/UIT/CE434.L21-Group3/Assignment_2/Output/bin_out_temp.txt");
       
        temp = shape[0] * shape[1];
        for (i=0; i < temp; i=i+1)
        begin
            
            RED   = mem[(temp * 0) + i];
            GREEN = mem[(temp * 1) + i];
            BLUE  = mem[(temp * 2) + i];
	        #80   
            if(i > 2)
                $fdisplay(write_data, "%b", GRAYSCALE);
        end
        for (i=0; i < 3; i=i+1)
        begin
            $fdisplay(write_data, "%b", GRAYSCALE);
        end

        $fclose(write_data);
        #500 $finish;
    end

    always @(CLK)
        #40 CLK <= ~CLK;

    rgb2grayscale dut (
        .grayscale  (GRAYSCALE),
        .dout_valid (DOUT_VALID), 
        .R          (RED), 
        .G          (GREEN), 
        .B          (BLUE), 
        .clk        (CLK), 
        .din_valid  (DIN_VALID)
    );
endmodule