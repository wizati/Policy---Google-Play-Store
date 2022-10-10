package Test2;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.*;

public class test1 {
	
	WebDriver driver;
	
	
	@BeforeMethod
	public void setupdriver() {
		System.setProperty("webdriver.chrome.driver", "C:\\chromedriver.exe");
		driver = new ChromeDriver();
		driver.get("https://testsheepnz.github.io/BasicCalculator.html");
	}
	
	@Test(priority = 1)
	public void getTitle() {
		String title = driver.getTitle();
		System.out.println(title);
		Assert.assertEquals("Basic Calculator", title);
	}
	
	@Test(priority=2)
	public void calculate() {
	driver.findElement(By.id("number1Field")).sendKeys("10");
	driver.findElement(By.id("number2Field")).sendKeys("10");
	
	WebElement calculate = driver.findElement(By.id("calculateButton"));
	calculate.click();
	String add = driver.findElement(By.id("numberAnswerField")).getAttribute("value").toString();
	Assert.assertEquals(add,"20");
	}
	

}
