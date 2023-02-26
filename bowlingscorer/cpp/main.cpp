#include "tenpin.hpp"

#include <string>
#include <iostream>

int main()
{
	std::cout << "Enter pins knocked down in each frame:" << std::endl;

	auto pins_knowcked_down = std::string{};
	std::cin >> pins_knowcked_down;

	std::cout << "Game score = " << ten_pin::score(pins_knowcked_down) << std::endl;

	return 0;
}
