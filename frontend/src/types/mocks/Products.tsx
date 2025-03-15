import type { Product } from "../Product";

export const simpleProduct: Product = {
    id: 1,
    name: 'Принтер',
    description: 'Незаменимая вещь для студента',
    price: 7000,
    category: 'Электроника',
};

export const productWithImage: Product = {
    id: 2,
    name: 'Настольная лампа',
    description: 'Говорят, что ее использовали в pixar',
    price: 699,
    category: 'Для дома',
    imgUrl: '/lamp.png',
};

export const productWithPriceSymbol: Product = {
    id: 3,
    name: 'Костюм гуся',
    description: 'Запускаем гуся, работяги',
    price: 1000,
    priceSymbol: '₽',
    category: 'Одежда',
};

export const productWithImageAndPriceSymbol: Product = {
    id: 4,
    name: 'IPhone 14 Pro',
    description: 'Latest iphone, buy it now',
    price: 999,
    priceSymbol: '$',
    category: 'Электроника',
    imgUrl: '/iphone.png',
};

export const productWithoutImage: Product = {
    id: 5,
    name: 'Принтер',
    description: 'Незаменимая вещь для студента',
    price: 7000,
    category: 'Электроника',
};
