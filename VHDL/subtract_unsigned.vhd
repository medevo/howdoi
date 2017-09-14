-- How do I subtract two std_logic_vectors unsigned

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use ieee.numeric_std.all;
entity alu is
    Port ( in1 : in  std_logic_vector(15 downto 0);
           in2 : in  std_logic_vector(15 downto 0);
           clk : in  STD_LOGIC; -- Just in case, this design is async
           result : out  std_logic_vector(15 downto 0));

end alu;

architecture Behavioral of alu is

begin

process(clk,in1,in2)
	variable tmp_s_16 : SIGNED (15 downto 0);
	variable tmp_l_16 : std_logic_vector(15 downto 0);
	
	tmp_s_16 := x"0000";
	tmp_l_16 := x"0000";

	-- Unsigned Subtract
	tmp_l_16 := STD_LOGIC_VECTOR(unsigned(in1) - unsigned(in2));
	tmp_s_16 := signed(tmp_l_16);

	result <= std_logic_vector(tmp_s_16);

	end process;			

end Behavioral;