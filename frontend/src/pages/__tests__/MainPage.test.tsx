import { render, fireEvent } from '@testing-library/react';
import { MainPage } from '../MainPage';
import '@testing-library/jest-dom';
import { Product } from '../../types';
import { useProducts } from '../../hooks';

describe('test MainPage', () => {
    it('should return render snapshot', () => {
        const r = render(<MainPage />);
        expect(r.asFragment()).toMatchSnapshot();
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
