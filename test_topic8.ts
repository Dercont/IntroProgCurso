// 1. Crear clase Persona.
// 2. Crear variables las privadas edad, nombre y telefono de la clase Persona.
// 3. Crear gets y sets de cada propiedad.
// 4. Crear un objeto persona en el main.
// 5. Utiliza los gets y sets para darle valores a las propiedades edad, nombre y telefono, por último muéstralas por consola.

//1.
class Person {
    //2.
    private name: string | null;
    private age: number | null;
    private phone: string | null;
    constructor(name: string | null = null, age: number | null = null, phone: string | null = null) {
        this.name = name;
        this.age = age;
        this.phone = phone;
    }
    //3.
    public getName(): string | null {
        return this.name;
    }
    public setName(name: string): void {
        this.name = name;
    }
    public getAge(): number | null {
        return this.age;
    }
    public setAge(age: number): void {
        this.age = age;
    }
    public getPhone(): string | null{
        return this.phone;
    }
    public setPhone(phone: string): void {
        this.phone = phone;
    }
}
//4.
const person = new Person();
// 5. Setters
person.setName("Alex Speed");
person.setAge(25);
person.setPhone("+50769210415");
// 5. Getters
console.log("Name:" , person.getName());
console.log("Age:", person.getAge());
console.log("Phone:", person.getPhone());