import { render, fireEvent } from '@testing-library/react';
import { MainPage } from '../MainPage';
import '@testing-library/jest-dom';
import { Product } from '../../types';
import { useProducts } from '../../hooks';

const FIXED_TIME = '00:00:00';

jest.mock('../../hooks', () => {
    const originalModule = jest.requireActual('../../hooks');
    return {
        ...originalModule, // <-- берем все реальные экспорты (включая useProducts)
        // а useCurrentTime переопределяем на зафиксированное значение
        useCurrentTime: jest.fn(() => FIXED_TIME),
    };
});

afterEach(jest.clearAllMocks);

describe('test MainPage', () => {
    it('should return render snapshot', () => {
        const mainPage = render(<MainPage />);
        expect(mainPage.asFragment()).toMatchSnapshot();
    });

    it('should display time from mock', () => {
        const mainPage = render(<MainPage />);
        // проверяем, что на странице появилось FIXED_TIME
        expect(mainPage.getByText(FIXED_TIME)).toBeInTheDocument();
    });

    it('should return filtered products if categories selected', () => {
        const mainPage = render(<MainPage />);
        const products: Product[] = useProducts();
        const electronicsCategories = mainPage.getAllByText('Электроника');
        const electronicsBadge = electronicsCategories.find((el) =>
            el.classList.contains('categories__badge')
        );

        if (!electronicsBadge) {
            throw new Error('Cant find category: "Электроника"');
        }

        fireEvent.click(electronicsBadge);
        products.forEach((product) => {
            if (product.category === 'Электроника') {
                expect(mainPage.getByText(product.name)).toBeInTheDocument();
            }
        });
    });
});
