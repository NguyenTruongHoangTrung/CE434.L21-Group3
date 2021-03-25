module rgb2grayscale(grayscale, dout_valid, R, G, B, clk, din_valid);
    parameter INT_WIDTH = 8;
    parameter FP_WIDTH = 16;
    output [INT_WIDTH-1:0] grayscale;
    output reg dout_valid;
    input  [INT_WIDTH-1:0] R,
                           G,
                           B;
    input clk;
    input din_valid;

    wire [FP_WIDTH-1:0] R_16 = {R[7:0], 8'd0};
    wire [FP_WIDTH-1:0] G_16 = {G[7:0], 8'd0};
    wire [FP_WIDTH-1:0] B_16 = {B[7:0], 8'd0};

    reg [FP_WIDTH-1:0] s0_0,
                       s0_1,
                       s0_2,
                       s0_3,
                       s0_4,
                       s0_5;

    reg [FP_WIDTH-1:0] s1_0,
                       s1_1,
                       s1_2;

    reg [FP_WIDTH-1:0] s2_0,
                       s2_1;

    reg [FP_WIDTH-1:0] s3_0;

    assign grayscale = s3_0[FP_WIDTH-1:INT_WIDTH];                              
    
    // State 0
    always @ (posedge clk)
    begin
        if(!din_valid)
        begin
            s0_0 <= 16'd0;
            s0_1 <= 16'd0;
            s0_2 <= 16'd0;
            s0_3 <= 16'd0;
            s0_4 <= 16'd0;
            s0_5 <= 16'd0;
        end
        else
        begin
            s0_0 <= R_16 >> 16'd2;
            s0_1 <= R_16 >> 16'd5;
            s0_2 <= G_16 >> 16'd1;
            s0_3 <= G_16 >> 16'd4;
            s0_4 <= B_16 >> 16'd4;
            s0_5 <= B_16 >> 16'd5;
        end
    end

    // State 1
    always @ (posedge clk)
    begin
        s1_0 <= s0_0 + s0_1;
        s1_1 <= s0_2 + s0_3;
        s1_2 <= s0_4 + s0_5;
    end

    // State 2
    always @ (posedge clk)
    begin
        s2_0 <= s1_0 + s1_1;
        s2_1 <= s1_2;
    end

    // State 3
    always @ (posedge clk) 
    begin
        s3_0 <= s2_0 + s2_1;
        dout_valid <= 1'b1;
    end
endmodule