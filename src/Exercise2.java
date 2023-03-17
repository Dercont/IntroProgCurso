public class Exercise2 {
    public static void main(String[] args) {
    //creating new object called "mycar"
        Car mycar = new Car();
    //adding new door to the car
        mycar.newDoor();
    }

    public static class Car {
        //properties
        int doors = 0;

        //methods
        public void newDoor(){
            this.doors++;
            System.out.println(doors);
        }

    }
}

