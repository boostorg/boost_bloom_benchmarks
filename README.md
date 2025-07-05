# Experimental results for [Boost Bloom Library](https://github.com/boostorg/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for several configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-march=native`),
which causes `fast_multiblock32` and `fast_multiblock64` to use their AVX2 variant.

For reference, we provide also insertion, successful lookup and unsuccessful lookup times
for a `boost::unordered_flat_set<int>` with the same number of elements `N`.

## Results

* [GCC 14, x64](#gcc-14-x64)
* [Clang 18, x64](#clang-18-x64)
* [Clang 15, ARM64](#clang-15-arm64)
* [VS 2022, x64](#vs-2022-x64)
* [GCC 14, x86](#gcc-14-x86)
* [Clang 18, x86](#clang-18-x86)
* [VS 2022, x86](#vs-2022-x86)

### GCC 14, x64
<!--gcc-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">38.33</td>
    <td align="right">5.81</td>
    <td align="right">4.28</td>
    <td align="right">12.72</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">11.10</td>
    <td align="right">11.92</td>
    <td align="right">18.46</td>
    <td align="right">17.05</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.00</td>
    <td align="right">4.34</td>
    <td align="right">4.67</td>
    <td align="right">11.20</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.45</td>
    <td align="right">4.78</td>
    <td align="right">5.14</td>
    <td align="right">11.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.69</td>
    <td align="right">18.09</td>
    <td align="right">19.31</td>
    <td align="right">20.95</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.39</td>
    <td align="right">4.85</td>
    <td align="right">4.83</td>
    <td align="right">11.61</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.02</td>
    <td align="right">5.42</td>
    <td align="right">5.21</td>
    <td align="right">11.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">20.45</td>
    <td align="right">21.48</td>
    <td align="right">18.13</td>
    <td align="right">23.15</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.02</td>
    <td align="right">5.38</td>
    <td align="right">5.06</td>
    <td align="right">12.04</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.56</td>
    <td align="right">5.75</td>
    <td align="right">5.67</td>
    <td align="right">12.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.31</td>
    <td align="right">27.68</td>
    <td align="right">18.44</td>
    <td align="right">27.29</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.39</td>
    <td align="right">5.72</td>
    <td align="right">5.62</td>
    <td align="right">12.37</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.82</td>
    <td align="right">6.04</td>
    <td align="right">5.95</td>
    <td align="right">12.83</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">11.13</td>
    <td align="right">13.18</td>
    <td align="right">13.64</td>
    <td align="right">19.34</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.00</td>
    <td align="right">4.34</td>
    <td align="right">4.67</td>
    <td align="right">11.16</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.46</td>
    <td align="right">4.80</td>
    <td align="right">5.17</td>
    <td align="right">11.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">16.63</td>
    <td align="right">20.66</td>
    <td align="right">17.97</td>
    <td align="right">27.04</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.39</td>
    <td align="right">4.85</td>
    <td align="right">4.82</td>
    <td align="right">11.62</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.01</td>
    <td align="right">5.42</td>
    <td align="right">5.20</td>
    <td align="right">11.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">20.37</td>
    <td align="right">24.67</td>
    <td align="right">21.29</td>
    <td align="right">31.14</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.02</td>
    <td align="right">5.38</td>
    <td align="right">5.07</td>
    <td align="right">12.04</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.56</td>
    <td align="right">5.75</td>
    <td align="right">5.67</td>
    <td align="right">12.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">24.30</td>
    <td align="right">29.48</td>
    <td align="right">25.66</td>
    <td align="right">36.39</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.38</td>
    <td align="right">5.72</td>
    <td align="right">5.61</td>
    <td align="right">12.36</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">5.81</td>
    <td align="right">6.03</td>
    <td align="right">5.95</td>
    <td align="right">12.83</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.03</td>
    <td align="right">5.77</td>
    <td align="right">14.45</td>
    <td align="right">13.06</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.50</td>
    <td align="right">7.35</td>
    <td align="right">15.00</td>
    <td align="right">12.96</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.23</td>
    <td align="right">3.14</td>
    <td align="right">3.64</td>
    <td align="right">12.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">5.86</td>
    <td align="right">8.49</td>
    <td align="right">15.06</td>
    <td align="right">14.33</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.04</td>
    <td align="right">9.41</td>
    <td align="right">16.38</td>
    <td align="right">15.70</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.72</td>
    <td align="right">2.96</td>
    <td align="right">2.87</td>
    <td align="right">11.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.13</td>
    <td align="right">12.19</td>
    <td align="right">16.24</td>
    <td align="right">17.18</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.14</td>
    <td align="right">12.21</td>
    <td align="right">17.42</td>
    <td align="right">17.90</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.78</td>
    <td align="right">6.31</td>
    <td align="right">4.19</td>
    <td align="right">15.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.39</td>
    <td align="right">13.51</td>
    <td align="right">15.42</td>
    <td align="right">18.39</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.68</td>
    <td align="right">14.33</td>
    <td align="right">17.80</td>
    <td align="right">19.61</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.82</td>
    <td align="right">6.33</td>
    <td align="right">4.13</td>
    <td align="right">15.15</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.04</td>
    <td align="right">5.99</td>
    <td align="right">6.17</td>
    <td align="right">12.59</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">5.50</td>
    <td align="right">7.22</td>
    <td align="right">7.26</td>
    <td align="right">13.65</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">3.24</td>
    <td align="right">3.15</td>
    <td align="right">3.64</td>
    <td align="right">12.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">5.86</td>
    <td align="right">8.06</td>
    <td align="right">8.03</td>
    <td align="right">14.24</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">7.04</td>
    <td align="right">9.54</td>
    <td align="right">9.37</td>
    <td align="right">16.77</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.73</td>
    <td align="right">2.94</td>
    <td align="right">2.87</td>
    <td align="right">11.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">9.02</td>
    <td align="right">11.91</td>
    <td align="right">11.24</td>
    <td align="right">17.03</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">19.12</td>
    <td align="right">13.33</td>
    <td align="right">13.24</td>
    <td align="right">20.11</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">5.79</td>
    <td align="right">5.83</td>
    <td align="right">5.59</td>
    <td align="right">14.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">10.37</td>
    <td align="right">12.73</td>
    <td align="right">12.74</td>
    <td align="right">18.97</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">11.56</td>
    <td align="right">14.79</td>
    <td align="right">14.53</td>
    <td align="right">21.63</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">5.84</td>
    <td align="right">5.86</td>
    <td align="right">5.60</td>
    <td align="right">14.34</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">3.16</td>
    <td align="right">2.97</td>
    <td align="right">3.39</td>
    <td align="right">11.71</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.61</td>
    <td align="right">4.70</td>
    <td align="right">5.02</td>
    <td align="right">14.63</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.81</td>
    <td align="right">4.48</td>
    <td align="right">4.76</td>
    <td align="right">14.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.33</td>
    <td align="right">3.08</td>
    <td align="right">2.94</td>
    <td align="right">11.77</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.50</td>
    <td align="right">4.25</td>
    <td align="right">4.11</td>
    <td align="right">14.27</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.83</td>
    <td align="right">4.62</td>
    <td align="right">4.60</td>
    <td align="right">14.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.55</td>
    <td align="right">5.87</td>
    <td align="right">3.90</td>
    <td align="right">14.57</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.59</td>
    <td align="right">8.29</td>
    <td align="right">6.27</td>
    <td align="right">17.86</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.78</td>
    <td align="right">8.12</td>
    <td align="right">6.13</td>
    <td align="right">17.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.61</td>
    <td align="right">5.90</td>
    <td align="right">3.89</td>
    <td align="right">15.47</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.51</td>
    <td align="right">9.36</td>
    <td align="right">6.12</td>
    <td align="right">19.07</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.65</td>
    <td align="right">9.11</td>
    <td align="right">6.24</td>
    <td align="right">18.62</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">3.18</td>
    <td align="right">2.95</td>
    <td align="right">3.36</td>
    <td align="right">11.72</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">4.65</td>
    <td align="right">4.72</td>
    <td align="right">5.04</td>
    <td align="right">14.64</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.79</td>
    <td align="right">4.47</td>
    <td align="right">4.78</td>
    <td align="right">14.45</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.31</td>
    <td align="right">3.04</td>
    <td align="right">2.95</td>
    <td align="right">11.83</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.46</td>
    <td align="right">4.27</td>
    <td align="right">4.07</td>
    <td align="right">14.41</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.81</td>
    <td align="right">4.61</td>
    <td align="right">4.48</td>
    <td align="right">14.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">5.55</td>
    <td align="right">5.54</td>
    <td align="right">5.35</td>
    <td align="right">13.78</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.56</td>
    <td align="right">8.07</td>
    <td align="right">7.98</td>
    <td align="right">17.43</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.85</td>
    <td align="right">7.86</td>
    <td align="right">7.85</td>
    <td align="right">16.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">5.62</td>
    <td align="right">5.58</td>
    <td align="right">5.33</td>
    <td align="right">13.84</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">8.42</td>
    <td align="right">8.64</td>
    <td align="right">8.56</td>
    <td align="right">17.66</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.63</td>
    <td align="right">8.72</td>
    <td align="right">8.49</td>
    <td align="right">17.63</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.42</td>
    <td align="right">7.27</td>
    <td align="right">14.88</td>
    <td align="right">13.28</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.75</td>
    <td align="right">8.59</td>
    <td align="right">19.10</td>
    <td align="right">15.90</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.31</td>
    <td align="right">11.43</td>
    <td align="right">20.02</td>
    <td align="right">16.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">8.78</td>
    <td align="right">10.14</td>
    <td align="right">14.53</td>
    <td align="right">16.13</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">12.56</td>
    <td align="right">10.32</td>
    <td align="right">16.42</td>
    <td align="right">17.29</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.98</td>
    <td align="right">13.68</td>
    <td align="right">20.53</td>
    <td align="right">19.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">10.65</td>
    <td align="right">11.50</td>
    <td align="right">13.87</td>
    <td align="right">16.66</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.98</td>
    <td align="right">12.75</td>
    <td align="right">17.31</td>
    <td align="right">19.50</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.34</td>
    <td align="right">14.62</td>
    <td align="right">18.98</td>
    <td align="right">19.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">12.86</td>
    <td align="right">14.15</td>
    <td align="right">15.14</td>
    <td align="right">18.13</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.63</td>
    <td align="right">14.97</td>
    <td align="right">16.85</td>
    <td align="right">20.10</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.63</td>
    <td align="right">20.29</td>
    <td align="right">21.20</td>
    <td align="right">23.06</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.43</td>
    <td align="right">7.10</td>
    <td align="right">7.32</td>
    <td align="right">13.45</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.74</td>
    <td align="right">8.84</td>
    <td align="right">8.96</td>
    <td align="right">16.10</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.17</td>
    <td align="right">11.06</td>
    <td align="right">11.28</td>
    <td align="right">18.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">8.78</td>
    <td align="right">10.03</td>
    <td align="right">10.00</td>
    <td align="right">16.46</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">12.54</td>
    <td align="right">11.02</td>
    <td align="right">10.94</td>
    <td align="right">18.03</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.09</td>
    <td align="right">14.69</td>
    <td align="right">14.39</td>
    <td align="right">21.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">10.67</td>
    <td align="right">11.31</td>
    <td align="right">11.25</td>
    <td align="right">17.58</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.99</td>
    <td align="right">13.94</td>
    <td align="right">13.21</td>
    <td align="right">20.57</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.27</td>
    <td align="right">16.49</td>
    <td align="right">15.28</td>
    <td align="right">22.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">12.86</td>
    <td align="right">14.24</td>
    <td align="right">14.12</td>
    <td align="right">20.04</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.64</td>
    <td align="right">16.05</td>
    <td align="right">15.96</td>
    <td align="right">21.70</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">20.75</td>
    <td align="right">21.24</td>
    <td align="right">21.13</td>
    <td align="right">26.47</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">58.16</td>
    <td align="right">25.77</td>
    <td align="right">14.32</td>
    <td align="right">32.46</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">15.33</td>
    <td align="right">16.86</td>
    <td align="right">21.39</td>
    <td align="right">20.76</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.64</td>
    <td align="right">5.53</td>
    <td align="right">5.83</td>
    <td align="right">12.41</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">6.77</td>
    <td align="right">7.50</td>
    <td align="right">7.55</td>
    <td align="right">13.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">44.18</td>
    <td align="right">47.73</td>
    <td align="right">26.78</td>
    <td align="right">38.57</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.63</td>
    <td align="right">11.05</td>
    <td align="right">11.05</td>
    <td align="right">17.83</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.90</td>
    <td align="right">12.33</td>
    <td align="right">12.05</td>
    <td align="right">17.60</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">85.57</td>
    <td align="right">93.40</td>
    <td align="right">33.64</td>
    <td align="right">66.29</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">16.75</td>
    <td align="right">18.23</td>
    <td align="right">17.76</td>
    <td align="right">23.33</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">18.76</td>
    <td align="right">18.66</td>
    <td align="right">18.55</td>
    <td align="right">23.88</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">124.55</td>
    <td align="right">133.01</td>
    <td align="right">38.97</td>
    <td align="right">90.63</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.86</td>
    <td align="right">21.77</td>
    <td align="right">21.63</td>
    <td align="right">26.84</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">22.82</td>
    <td align="right">25.01</td>
    <td align="right">22.33</td>
    <td align="right">28.86</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">12.87</td>
    <td align="right">15.30</td>
    <td align="right">14.97</td>
    <td align="right">21.48</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.78</td>
    <td align="right">6.23</td>
    <td align="right">6.48</td>
    <td align="right">13.04</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.47</td>
    <td align="right">5.85</td>
    <td align="right">6.27</td>
    <td align="right">14.01</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">50.87</td>
    <td align="right">55.16</td>
    <td align="right">47.57</td>
    <td align="right">57.05</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.31</td>
    <td align="right">10.70</td>
    <td align="right">10.64</td>
    <td align="right">16.56</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.34</td>
    <td align="right">12.19</td>
    <td align="right">11.89</td>
    <td align="right">17.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">83.94</td>
    <td align="right">84.09</td>
    <td align="right">74.14</td>
    <td align="right">84.14</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">17.61</td>
    <td align="right">18.26</td>
    <td align="right">17.74</td>
    <td align="right">23.40</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">19.23</td>
    <td align="right">19.11</td>
    <td align="right">19.00</td>
    <td align="right">24.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">125.08</td>
    <td align="right">127.96</td>
    <td align="right">107.35</td>
    <td align="right">131.12</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.79</td>
    <td align="right">21.66</td>
    <td align="right">21.51</td>
    <td align="right">26.77</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">22.79</td>
    <td align="right">24.95</td>
    <td align="right">22.29</td>
    <td align="right">28.80</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.29</td>
    <td align="right">7.05</td>
    <td align="right">15.56</td>
    <td align="right">14.17</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">6.50</td>
    <td align="right">8.71</td>
    <td align="right">16.59</td>
    <td align="right">14.80</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.81</td>
    <td align="right">3.70</td>
    <td align="right">4.44</td>
    <td align="right">12.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.08</td>
    <td align="right">15.54</td>
    <td align="right">19.45</td>
    <td align="right">20.35</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.59</td>
    <td align="right">18.93</td>
    <td align="right">23.59</td>
    <td align="right">23.27</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.48</td>
    <td align="right">8.19</td>
    <td align="right">7.79</td>
    <td align="right">15.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.99</td>
    <td align="right">31.25</td>
    <td align="right">24.63</td>
    <td align="right">31.13</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">34.48</td>
    <td align="right">31.04</td>
    <td align="right">27.27</td>
    <td align="right">32.94</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">19.02</td>
    <td align="right">20.98</td>
    <td align="right">14.84</td>
    <td align="right">25.91</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">38.51</td>
    <td align="right">38.80</td>
    <td align="right">27.51</td>
    <td align="right">39.51</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.93</td>
    <td align="right">43.03</td>
    <td align="right">32.30</td>
    <td align="right">44.96</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">22.10</td>
    <td align="right">24.23</td>
    <td align="right">16.69</td>
    <td align="right">28.64</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">5.83</td>
    <td align="right">6.85</td>
    <td align="right">7.04</td>
    <td align="right">14.18</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">7.09</td>
    <td align="right">9.13</td>
    <td align="right">9.10</td>
    <td align="right">15.97</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.88</td>
    <td align="right">4.87</td>
    <td align="right">5.33</td>
    <td align="right">13.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">13.80</td>
    <td align="right">16.16</td>
    <td align="right">16.11</td>
    <td align="right">22.01</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.21</td>
    <td align="right">18.73</td>
    <td align="right">17.75</td>
    <td align="right">24.64</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.16</td>
    <td align="right">7.77</td>
    <td align="right">7.46</td>
    <td align="right">15.04</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">29.89</td>
    <td align="right">31.05</td>
    <td align="right">30.63</td>
    <td align="right">35.34</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">35.07</td>
    <td align="right">33.39</td>
    <td align="right">33.35</td>
    <td align="right">38.81</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">19.12</td>
    <td align="right">20.77</td>
    <td align="right">20.21</td>
    <td align="right">26.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">38.56</td>
    <td align="right">39.57</td>
    <td align="right">39.12</td>
    <td align="right">44.42</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">40.70</td>
    <td align="right">50.09</td>
    <td align="right">49.61</td>
    <td align="right">55.68</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">22.03</td>
    <td align="right">23.81</td>
    <td align="right">23.13</td>
    <td align="right">29.93</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.82</td>
    <td align="right">3.56</td>
    <td align="right">4.17</td>
    <td align="right">12.26</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">5.66</td>
    <td align="right">5.89</td>
    <td align="right">6.23</td>
    <td align="right">15.91</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">6.71</td>
    <td align="right">6.76</td>
    <td align="right">6.85</td>
    <td align="right">15.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.68</td>
    <td align="right">9.01</td>
    <td align="right">8.54</td>
    <td align="right">15.21</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">8.96</td>
    <td align="right">10.06</td>
    <td align="right">9.80</td>
    <td align="right">18.22</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.72</td>
    <td align="right">11.73</td>
    <td align="right">11.44</td>
    <td align="right">18.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.61</td>
    <td align="right">20.69</td>
    <td align="right">14.63</td>
    <td align="right">25.46</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">25.08</td>
    <td align="right">26.26</td>
    <td align="right">21.51</td>
    <td align="right">31.18</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">24.20</td>
    <td align="right">26.78</td>
    <td align="right">21.88</td>
    <td align="right">31.23</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">22.00</td>
    <td align="right">24.05</td>
    <td align="right">16.51</td>
    <td align="right">27.46</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">32.47</td>
    <td align="right">36.50</td>
    <td align="right">24.91</td>
    <td align="right">38.90</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">31.96</td>
    <td align="right">36.51</td>
    <td align="right">25.07</td>
    <td align="right">37.57</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.48</td>
    <td align="right">4.41</td>
    <td align="right">4.80</td>
    <td align="right">12.68</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">6.10</td>
    <td align="right">6.42</td>
    <td align="right">6.63</td>
    <td align="right">16.12</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.88</td>
    <td align="right">5.77</td>
    <td align="right">6.04</td>
    <td align="right">15.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">8.53</td>
    <td align="right">8.87</td>
    <td align="right">8.45</td>
    <td align="right">15.09</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.03</td>
    <td align="right">10.20</td>
    <td align="right">9.88</td>
    <td align="right">18.13</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">11.14</td>
    <td align="right">12.18</td>
    <td align="right">11.39</td>
    <td align="right">18.87</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">18.58</td>
    <td align="right">20.41</td>
    <td align="right">20.00</td>
    <td align="right">25.45</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">24.63</td>
    <td align="right">25.68</td>
    <td align="right">25.53</td>
    <td align="right">32.03</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">24.22</td>
    <td align="right">26.55</td>
    <td align="right">26.52</td>
    <td align="right">33.76</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">21.89</td>
    <td align="right">23.78</td>
    <td align="right">23.16</td>
    <td align="right">29.45</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">32.21</td>
    <td align="right">35.52</td>
    <td align="right">31.65</td>
    <td align="right">38.42</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">31.89</td>
    <td align="right">36.23</td>
    <td align="right">32.12</td>
    <td align="right">37.97</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.52</td>
    <td align="right">9.34</td>
    <td align="right">16.39</td>
    <td align="right">15.35</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.67</td>
    <td align="right">10.24</td>
    <td align="right">20.74</td>
    <td align="right">18.07</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.12</td>
    <td align="right">14.57</td>
    <td align="right">21.98</td>
    <td align="right">19.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">16.28</td>
    <td align="right">17.60</td>
    <td align="right">19.83</td>
    <td align="right">22.82</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">22.29</td>
    <td align="right">21.06</td>
    <td align="right">21.82</td>
    <td align="right">25.46</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">29.72</td>
    <td align="right">30.94</td>
    <td align="right">27.60</td>
    <td align="right">31.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.36</td>
    <td align="right">27.65</td>
    <td align="right">21.74</td>
    <td align="right">30.65</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.90</td>
    <td align="right">33.23</td>
    <td align="right">26.34</td>
    <td align="right">36.86</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">46.01</td>
    <td align="right">46.87</td>
    <td align="right">33.47</td>
    <td align="right">42.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">41.70</td>
    <td align="right">42.35</td>
    <td align="right">25.41</td>
    <td align="right">42.49</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">51.25</td>
    <td align="right">50.49</td>
    <td align="right">29.48</td>
    <td align="right">48.96</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">74.78</td>
    <td align="right">70.29</td>
    <td align="right">40.75</td>
    <td align="right">57.39</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.10</td>
    <td align="right">8.83</td>
    <td align="right">9.01</td>
    <td align="right">15.68</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.88</td>
    <td align="right">10.95</td>
    <td align="right">11.09</td>
    <td align="right">18.77</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.73</td>
    <td align="right">15.15</td>
    <td align="right">15.32</td>
    <td align="right">21.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">18.30</td>
    <td align="right">19.48</td>
    <td align="right">19.33</td>
    <td align="right">25.53</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">20.79</td>
    <td align="right">20.39</td>
    <td align="right">20.40</td>
    <td align="right">26.68</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">29.60</td>
    <td align="right">32.40</td>
    <td align="right">32.09</td>
    <td align="right">38.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">27.34</td>
    <td align="right">32.41</td>
    <td align="right">29.13</td>
    <td align="right">34.56</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">34.86</td>
    <td align="right">40.28</td>
    <td align="right">39.45</td>
    <td align="right">45.90</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.39</td>
    <td align="right">50.00</td>
    <td align="right">49.25</td>
    <td align="right">54.55</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">41.55</td>
    <td align="right">42.81</td>
    <td align="right">42.64</td>
    <td align="right">47.99</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">50.80</td>
    <td align="right">51.20</td>
    <td align="right">51.14</td>
    <td align="right">56.26</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">74.76</td>
    <td align="right">74.16</td>
    <td align="right">73.81</td>
    <td align="right">78.68</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.11</td>
    <td align="right">5.96</td>
    <td align="right">3.95</td>
    <td align="right">12.90</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.36</td>
    <td align="right">11.73</td>
    <td align="right">17.57</td>
    <td align="right">16.66</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.06</td>
    <td align="right">4.62</td>
    <td align="right">4.62</td>
    <td align="right">4.62</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.07</td>
    <td align="right">4.92</td>
    <td align="right">4.93</td>
    <td align="right">4.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.67</td>
    <td align="right">17.15</td>
    <td align="right">18.48</td>
    <td align="right">20.19</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.60</td>
    <td align="right">5.32</td>
    <td align="right">5.32</td>
    <td align="right">5.32</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.57</td>
    <td align="right">5.51</td>
    <td align="right">5.51</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.73</td>
    <td align="right">20.40</td>
    <td align="right">17.27</td>
    <td align="right">22.70</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.99</td>
    <td align="right">5.75</td>
    <td align="right">5.75</td>
    <td align="right">5.75</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.94</td>
    <td align="right">5.93</td>
    <td align="right">5.93</td>
    <td align="right">5.93</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.18</td>
    <td align="right">24.63</td>
    <td align="right">17.68</td>
    <td align="right">25.20</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.41</td>
    <td align="right">6.26</td>
    <td align="right">6.26</td>
    <td align="right">6.27</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.30</td>
    <td align="right">3.75</td>
    <td align="right">3.75</td>
    <td align="right">3.75</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.30</td>
    <td align="right">11.02</td>
    <td align="right">11.05</td>
    <td align="right">11.05</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">4.06</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
    <td align="right">4.62</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.08</td>
    <td align="right">4.93</td>
    <td align="right">4.94</td>
    <td align="right">4.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.66</td>
    <td align="right">15.15</td>
    <td align="right">15.15</td>
    <td align="right">15.23</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.58</td>
    <td align="right">5.33</td>
    <td align="right">5.32</td>
    <td align="right">5.32</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">4.57</td>
    <td align="right">5.51</td>
    <td align="right">5.51</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.89</td>
    <td align="right">18.33</td>
    <td align="right">18.41</td>
    <td align="right">18.30</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">4.99</td>
    <td align="right">5.76</td>
    <td align="right">5.76</td>
    <td align="right">5.76</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">4.91</td>
    <td align="right">5.90</td>
    <td align="right">5.90</td>
    <td align="right">5.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.44</td>
    <td align="right">25.49</td>
    <td align="right">25.31</td>
    <td align="right">25.32</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.42</td>
    <td align="right">6.27</td>
    <td align="right">6.27</td>
    <td align="right">6.27</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">3.32</td>
    <td align="right">3.74</td>
    <td align="right">3.74</td>
    <td align="right">3.74</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.25</td>
    <td align="right">6.37</td>
    <td align="right">13.72</td>
    <td align="right">12.14</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.33</td>
    <td align="right">6.32</td>
    <td align="right">14.69</td>
    <td align="right">11.78</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.90</td>
    <td align="right">3.37</td>
    <td align="right">3.37</td>
    <td align="right">3.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.39</td>
    <td align="right">8.88</td>
    <td align="right">14.88</td>
    <td align="right">14.09</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.05</td>
    <td align="right">8.92</td>
    <td align="right">14.74</td>
    <td align="right">14.00</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.77</td>
    <td align="right">3.19</td>
    <td align="right">3.19</td>
    <td align="right">3.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.85</td>
    <td align="right">12.19</td>
    <td align="right">15.82</td>
    <td align="right">16.80</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">6.03</td>
    <td align="right">11.93</td>
    <td align="right">15.43</td>
    <td align="right">16.29</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.41</td>
    <td align="right">4.60</td>
    <td align="right">2.98</td>
    <td align="right">13.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.27</td>
    <td align="right">13.54</td>
    <td align="right">15.66</td>
    <td align="right">18.23</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">6.95</td>
    <td align="right">13.55</td>
    <td align="right">15.75</td>
    <td align="right">18.16</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.47</td>
    <td align="right">4.62</td>
    <td align="right">2.93</td>
    <td align="right">13.89</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">3.27</td>
    <td align="right">6.32</td>
    <td align="right">6.32</td>
    <td align="right">6.33</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">3.32</td>
    <td align="right">6.23</td>
    <td align="right">6.24</td>
    <td align="right">6.23</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.90</td>
    <td align="right">3.37</td>
    <td align="right">3.37</td>
    <td align="right">3.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">3.38</td>
    <td align="right">5.34</td>
    <td align="right">5.34</td>
    <td align="right">5.34</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">4.04</td>
    <td align="right">5.49</td>
    <td align="right">5.51</td>
    <td align="right">5.51</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.76</td>
    <td align="right">3.18</td>
    <td align="right">3.19</td>
    <td align="right">3.19</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">5.86</td>
    <td align="right">8.09</td>
    <td align="right">8.15</td>
    <td align="right">8.14</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">6.01</td>
    <td align="right">7.91</td>
    <td align="right">7.93</td>
    <td align="right">7.96</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.39</td>
    <td align="right">4.85</td>
    <td align="right">4.85</td>
    <td align="right">4.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">6.26</td>
    <td align="right">8.66</td>
    <td align="right">8.76</td>
    <td align="right">8.77</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">7.03</td>
    <td align="right">8.94</td>
    <td align="right">9.05</td>
    <td align="right">8.96</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.48</td>
    <td align="right">4.89</td>
    <td align="right">4.88</td>
    <td align="right">4.88</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.84</td>
    <td align="right">3.12</td>
    <td align="right">3.12</td>
    <td align="right">3.15</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.92</td>
    <td align="right">4.46</td>
    <td align="right">4.46</td>
    <td align="right">4.46</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.07</td>
    <td align="right">4.22</td>
    <td align="right">4.22</td>
    <td align="right">4.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.96</td>
    <td align="right">3.19</td>
    <td align="right">3.21</td>
    <td align="right">3.21</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.51</td>
    <td align="right">4.25</td>
    <td align="right">4.25</td>
    <td align="right">4.25</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.25</td>
    <td align="right">4.31</td>
    <td align="right">4.31</td>
    <td align="right">4.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.47</td>
    <td align="right">4.35</td>
    <td align="right">2.77</td>
    <td align="right">13.38</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.81</td>
    <td align="right">6.45</td>
    <td align="right">4.77</td>
    <td align="right">16.74</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">6.09</td>
    <td align="right">6.20</td>
    <td align="right">4.61</td>
    <td align="right">16.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.54</td>
    <td align="right">4.43</td>
    <td align="right">2.73</td>
    <td align="right">13.23</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.96</td>
    <td align="right">7.20</td>
    <td align="right">4.81</td>
    <td align="right">17.40</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.32</td>
    <td align="right">7.02</td>
    <td align="right">4.71</td>
    <td align="right">16.99</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.86</td>
    <td align="right">3.12</td>
    <td align="right">3.12</td>
    <td align="right">3.13</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.89</td>
    <td align="right">4.44</td>
    <td align="right">4.44</td>
    <td align="right">4.45</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">4.08</td>
    <td align="right">4.23</td>
    <td align="right">4.23</td>
    <td align="right">4.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.95</td>
    <td align="right">3.20</td>
    <td align="right">3.21</td>
    <td align="right">3.21</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">3.49</td>
    <td align="right">4.25</td>
    <td align="right">4.25</td>
    <td align="right">4.25</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">4.28</td>
    <td align="right">4.32</td>
    <td align="right">4.32</td>
    <td align="right">4.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.46</td>
    <td align="right">4.59</td>
    <td align="right">4.59</td>
    <td align="right">4.59</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">5.84</td>
    <td align="right">6.75</td>
    <td align="right">6.76</td>
    <td align="right">6.74</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">6.05</td>
    <td align="right">6.54</td>
    <td align="right">6.55</td>
    <td align="right">6.33</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.54</td>
    <td align="right">4.61</td>
    <td align="right">4.61</td>
    <td align="right">4.60</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">6.99</td>
    <td align="right">7.86</td>
    <td align="right">7.86</td>
    <td align="right">7.86</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">7.22</td>
    <td align="right">7.60</td>
    <td align="right">7.59</td>
    <td align="right">7.60</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.34</td>
    <td align="right">7.43</td>
    <td align="right">14.00</td>
    <td align="right">13.06</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.77</td>
    <td align="right">7.89</td>
    <td align="right">17.89</td>
    <td align="right">14.88</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.40</td>
    <td align="right">11.09</td>
    <td align="right">18.80</td>
    <td align="right">16.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.60</td>
    <td align="right">9.81</td>
    <td align="right">13.52</td>
    <td align="right">15.63</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.56</td>
    <td align="right">10.08</td>
    <td align="right">14.95</td>
    <td align="right">16.36</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.63</td>
    <td align="right">14.15</td>
    <td align="right">20.31</td>
    <td align="right">19.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.99</td>
    <td align="right">11.44</td>
    <td align="right">13.70</td>
    <td align="right">16.30</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">15.53</td>
    <td align="right">12.48</td>
    <td align="right">16.28</td>
    <td align="right">18.67</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.77</td>
    <td align="right">14.97</td>
    <td align="right">18.76</td>
    <td align="right">19.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.30</td>
    <td align="right">13.46</td>
    <td align="right">14.24</td>
    <td align="right">18.11</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.18</td>
    <td align="right">13.66</td>
    <td align="right">15.80</td>
    <td align="right">19.69</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.52</td>
    <td align="right">20.31</td>
    <td align="right">22.79</td>
    <td align="right">22.95</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">6.33</td>
    <td align="right">7.42</td>
    <td align="right">7.43</td>
    <td align="right">7.42</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">11.75</td>
    <td align="right">8.92</td>
    <td align="right">8.92</td>
    <td align="right">8.93</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.04</td>
    <td align="right">11.45</td>
    <td align="right">11.63</td>
    <td align="right">11.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.72</td>
    <td align="right">10.09</td>
    <td align="right">10.10</td>
    <td align="right">10.09</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">13.58</td>
    <td align="right">10.66</td>
    <td align="right">10.65</td>
    <td align="right">10.65</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">14.78</td>
    <td align="right">15.71</td>
    <td align="right">15.78</td>
    <td align="right">15.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.98</td>
    <td align="right">11.81</td>
    <td align="right">11.81</td>
    <td align="right">11.80</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">16.14</td>
    <td align="right">13.25</td>
    <td align="right">13.25</td>
    <td align="right">13.25</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.87</td>
    <td align="right">16.40</td>
    <td align="right">16.48</td>
    <td align="right">16.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.32</td>
    <td align="right">14.27</td>
    <td align="right">14.28</td>
    <td align="right">14.30</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">17.12</td>
    <td align="right">15.59</td>
    <td align="right">15.59</td>
    <td align="right">15.60</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">21.67</td>
    <td align="right">21.34</td>
    <td align="right">21.46</td>
    <td align="right">21.37</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">52.12</td>
    <td align="right">23.72</td>
    <td align="right">13.31</td>
    <td align="right">30.57</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">14.75</td>
    <td align="right">16.24</td>
    <td align="right">20.23</td>
    <td align="right">19.85</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.28</td>
    <td align="right">5.82</td>
    <td align="right">5.86</td>
    <td align="right">5.85</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.19</td>
    <td align="right">6.21</td>
    <td align="right">6.11</td>
    <td align="right">6.11</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">48.37</td>
    <td align="right">52.56</td>
    <td align="right">25.79</td>
    <td align="right">39.74</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">10.23</td>
    <td align="right">11.16</td>
    <td align="right">11.15</td>
    <td align="right">11.16</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">11.15</td>
    <td align="right">12.40</td>
    <td align="right">12.71</td>
    <td align="right">12.40</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">82.94</td>
    <td align="right">86.38</td>
    <td align="right">29.63</td>
    <td align="right">60.89</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">18.06</td>
    <td align="right">18.56</td>
    <td align="right">18.57</td>
    <td align="right">18.57</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.86</td>
    <td align="right">18.79</td>
    <td align="right">18.76</td>
    <td align="right">18.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">120.89</td>
    <td align="right">120.75</td>
    <td align="right">34.63</td>
    <td align="right">82.15</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">22.01</td>
    <td align="right">24.93</td>
    <td align="right">24.97</td>
    <td align="right">24.95</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.72</td>
    <td align="right">16.79</td>
    <td align="right">16.79</td>
    <td align="right">16.79</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">14.54</td>
    <td align="right">15.44</td>
    <td align="right">15.55</td>
    <td align="right">15.50</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">5.27</td>
    <td align="right">5.80</td>
    <td align="right">5.80</td>
    <td align="right">5.79</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">5.53</td>
    <td align="right">6.48</td>
    <td align="right">6.55</td>
    <td align="right">6.50</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">46.58</td>
    <td align="right">41.33</td>
    <td align="right">41.33</td>
    <td align="right">41.37</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">11.68</td>
    <td align="right">12.79</td>
    <td align="right">12.76</td>
    <td align="right">12.79</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">10.99</td>
    <td align="right">12.38</td>
    <td align="right">12.22</td>
    <td align="right">12.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">82.58</td>
    <td align="right">70.10</td>
    <td align="right">70.09</td>
    <td align="right">70.09</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">17.97</td>
    <td align="right">18.45</td>
    <td align="right">18.46</td>
    <td align="right">18.46</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">17.06</td>
    <td align="right">18.98</td>
    <td align="right">18.99</td>
    <td align="right">18.97</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">121.64</td>
    <td align="right">107.98</td>
    <td align="right">107.52</td>
    <td align="right">107.41</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">21.96</td>
    <td align="right">24.89</td>
    <td align="right">24.89</td>
    <td align="right">24.88</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">14.59</td>
    <td align="right">16.61</td>
    <td align="right">16.61</td>
    <td align="right">16.61</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">4.04</td>
    <td align="right">7.65</td>
    <td align="right">14.46</td>
    <td align="right">13.88</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">5.99</td>
    <td align="right">10.01</td>
    <td align="right">15.96</td>
    <td align="right">15.01</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.26</td>
    <td align="right">5.01</td>
    <td align="right">4.98</td>
    <td align="right">4.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.59</td>
    <td align="right">15.65</td>
    <td align="right">18.20</td>
    <td align="right">20.15</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">10.06</td>
    <td align="right">18.96</td>
    <td align="right">18.72</td>
    <td align="right">21.20</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.96</td>
    <td align="right">8.81</td>
    <td align="right">8.83</td>
    <td align="right">8.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">19.19</td>
    <td align="right">30.12</td>
    <td align="right">23.83</td>
    <td align="right">30.75</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.99</td>
    <td align="right">30.82</td>
    <td align="right">23.12</td>
    <td align="right">30.58</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.22</td>
    <td align="right">16.34</td>
    <td align="right">10.99</td>
    <td align="right">21.08</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">24.00</td>
    <td align="right">40.18</td>
    <td align="right">26.78</td>
    <td align="right">40.08</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.97</td>
    <td align="right">41.15</td>
    <td align="right">27.01</td>
    <td align="right">40.84</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.65</td>
    <td align="right">18.41</td>
    <td align="right">12.24</td>
    <td align="right">23.53</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">4.05</td>
    <td align="right">7.48</td>
    <td align="right">7.47</td>
    <td align="right">7.47</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">4.32</td>
    <td align="right">7.83</td>
    <td align="right">7.88</td>
    <td align="right">7.91</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">4.17</td>
    <td align="right">4.90</td>
    <td align="right">4.91</td>
    <td align="right">4.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">8.80</td>
    <td align="right">11.35</td>
    <td align="right">11.31</td>
    <td align="right">11.39</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">9.53</td>
    <td align="right">13.01</td>
    <td align="right">13.06</td>
    <td align="right">13.05</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">7.65</td>
    <td align="right">8.43</td>
    <td align="right">8.39</td>
    <td align="right">8.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">19.69</td>
    <td align="right">24.58</td>
    <td align="right">24.60</td>
    <td align="right">24.60</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.72</td>
    <td align="right">24.74</td>
    <td align="right">24.73</td>
    <td align="right">24.74</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">15.19</td>
    <td align="right">16.50</td>
    <td align="right">16.50</td>
    <td align="right">16.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">23.95</td>
    <td align="right">30.74</td>
    <td align="right">30.77</td>
    <td align="right">30.77</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">24.85</td>
    <td align="right">31.62</td>
    <td align="right">31.62</td>
    <td align="right">31.57</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">17.45</td>
    <td align="right">18.56</td>
    <td align="right">18.56</td>
    <td align="right">18.57</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.86</td>
    <td align="right">4.39</td>
    <td align="right">4.37</td>
    <td align="right">4.42</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.83</td>
    <td align="right">5.39</td>
    <td align="right">5.40</td>
    <td align="right">5.41</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.87</td>
    <td align="right">5.17</td>
    <td align="right">5.15</td>
    <td align="right">5.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.76</td>
    <td align="right">9.18</td>
    <td align="right">9.21</td>
    <td align="right">9.18</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.45</td>
    <td align="right">10.46</td>
    <td align="right">10.51</td>
    <td align="right">10.50</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.41</td>
    <td align="right">11.91</td>
    <td align="right">11.88</td>
    <td align="right">11.89</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.35</td>
    <td align="right">16.14</td>
    <td align="right">10.33</td>
    <td align="right">20.37</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.89</td>
    <td align="right">21.23</td>
    <td align="right">16.18</td>
    <td align="right">26.85</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">18.88</td>
    <td align="right">21.22</td>
    <td align="right">15.55</td>
    <td align="right">26.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.62</td>
    <td align="right">18.39</td>
    <td align="right">11.60</td>
    <td align="right">22.55</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.15</td>
    <td align="right">29.46</td>
    <td align="right">18.61</td>
    <td align="right">32.50</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">25.58</td>
    <td align="right">26.93</td>
    <td align="right">17.71</td>
    <td align="right">31.62</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">4.16</td>
    <td align="right">4.64</td>
    <td align="right">4.61</td>
    <td align="right">4.66</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.96</td>
    <td align="right">5.68</td>
    <td align="right">5.70</td>
    <td align="right">5.70</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">5.26</td>
    <td align="right">5.67</td>
    <td align="right">5.71</td>
    <td align="right">5.63</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">7.68</td>
    <td align="right">9.11</td>
    <td align="right">9.11</td>
    <td align="right">9.14</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">9.73</td>
    <td align="right">10.78</td>
    <td align="right">10.78</td>
    <td align="right">10.77</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">10.30</td>
    <td align="right">11.79</td>
    <td align="right">11.73</td>
    <td align="right">11.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.53</td>
    <td align="right">16.50</td>
    <td align="right">16.51</td>
    <td align="right">16.53</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">19.85</td>
    <td align="right">21.66</td>
    <td align="right">21.65</td>
    <td align="right">21.68</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">19.82</td>
    <td align="right">22.81</td>
    <td align="right">22.81</td>
    <td align="right">22.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">16.69</td>
    <td align="right">18.59</td>
    <td align="right">18.59</td>
    <td align="right">18.58</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">25.10</td>
    <td align="right">30.71</td>
    <td align="right">30.72</td>
    <td align="right">30.72</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">25.58</td>
    <td align="right">32.46</td>
    <td align="right">31.57</td>
    <td align="right">31.21</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.27</td>
    <td align="right">9.42</td>
    <td align="right">15.48</td>
    <td align="right">15.59</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">12.75</td>
    <td align="right">9.87</td>
    <td align="right">19.30</td>
    <td align="right">17.16</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">14.15</td>
    <td align="right">14.49</td>
    <td align="right">20.62</td>
    <td align="right">18.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">17.65</td>
    <td align="right">17.32</td>
    <td align="right">17.51</td>
    <td align="right">22.06</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.90</td>
    <td align="right">22.24</td>
    <td align="right">19.32</td>
    <td align="right">25.23</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">26.89</td>
    <td align="right">25.79</td>
    <td align="right">25.38</td>
    <td align="right">27.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.55</td>
    <td align="right">27.08</td>
    <td align="right">21.59</td>
    <td align="right">29.76</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">36.66</td>
    <td align="right">33.44</td>
    <td align="right">24.76</td>
    <td align="right">36.33</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.51</td>
    <td align="right">43.22</td>
    <td align="right">29.88</td>
    <td align="right">39.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">43.27</td>
    <td align="right">40.94</td>
    <td align="right">24.65</td>
    <td align="right">42.26</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">52.70</td>
    <td align="right">40.41</td>
    <td align="right">26.50</td>
    <td align="right">43.53</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">78.83</td>
    <td align="right">70.16</td>
    <td align="right">40.83</td>
    <td align="right">57.24</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">8.03</td>
    <td align="right">9.23</td>
    <td align="right">9.21</td>
    <td align="right">9.20</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">13.89</td>
    <td align="right">11.87</td>
    <td align="right">11.88</td>
    <td align="right">11.92</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">13.60</td>
    <td align="right">14.38</td>
    <td align="right">14.48</td>
    <td align="right">14.49</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">18.33</td>
    <td align="right">18.39</td>
    <td align="right">18.39</td>
    <td align="right">18.40</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">23.71</td>
    <td align="right">22.21</td>
    <td align="right">22.38</td>
    <td align="right">22.26</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">26.04</td>
    <td align="right">27.49</td>
    <td align="right">27.54</td>
    <td align="right">27.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">29.18</td>
    <td align="right">32.33</td>
    <td align="right">32.34</td>
    <td align="right">32.29</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">36.51</td>
    <td align="right">40.10</td>
    <td align="right">40.08</td>
    <td align="right">40.08</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">45.12</td>
    <td align="right">49.01</td>
    <td align="right">49.35</td>
    <td align="right">49.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">43.23</td>
    <td align="right">42.89</td>
    <td align="right">42.85</td>
    <td align="right">42.84</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">52.70</td>
    <td align="right">51.24</td>
    <td align="right">51.23</td>
    <td align="right">51.24</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">78.54</td>
    <td align="right">74.76</td>
    <td align="right">74.74</td>
    <td align="right">74.82</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">18.71</td>
    <td align="right">2.55</td>
    <td align="right">1.95</td>
    <td align="right">9.33</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">6.33</td>
    <td align="right">4.32</td>
    <td align="right">11.33</td>
    <td align="right">8.94</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.31</td>
    <td align="right">1.51</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.62</td>
    <td align="right">1.48</td>
    <td align="right">1.48</td>
    <td align="right">1.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.44</td>
    <td align="right">6.21</td>
    <td align="right">11.68</td>
    <td align="right">10.28</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.42</td>
    <td align="right">1.70</td>
    <td align="right">1.69</td>
    <td align="right">1.69</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.68</td>
    <td align="right">1.65</td>
    <td align="right">1.66</td>
    <td align="right">1.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.54</td>
    <td align="right">7.40</td>
    <td align="right">10.82</td>
    <td align="right">11.01</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.60</td>
    <td align="right">1.91</td>
    <td align="right">1.91</td>
    <td align="right">1.91</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.76</td>
    <td align="right">1.85</td>
    <td align="right">1.84</td>
    <td align="right">1.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">15.00</td>
    <td align="right">9.47</td>
    <td align="right">11.05</td>
    <td align="right">12.86</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.82</td>
    <td align="right">2.13</td>
    <td align="right">2.12</td>
    <td align="right">2.10</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.81</td>
    <td align="right">1.62</td>
    <td align="right">1.62</td>
    <td align="right">1.62</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">6.34</td>
    <td align="right">3.94</td>
    <td align="right">3.94</td>
    <td align="right">3.94</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">1.29</td>
    <td align="right">1.50</td>
    <td align="right">1.50</td>
    <td align="right">1.49</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">1.61</td>
    <td align="right">1.46</td>
    <td align="right">1.47</td>
    <td align="right">1.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">9.50</td>
    <td align="right">5.89</td>
    <td align="right">5.91</td>
    <td align="right">5.89</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">1.42</td>
    <td align="right">1.71</td>
    <td align="right">1.71</td>
    <td align="right">1.71</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">1.69</td>
    <td align="right">1.67</td>
    <td align="right">1.67</td>
    <td align="right">1.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">11.65</td>
    <td align="right">7.13</td>
    <td align="right">7.11</td>
    <td align="right">7.12</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">1.61</td>
    <td align="right">1.92</td>
    <td align="right">1.91</td>
    <td align="right">1.91</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">1.76</td>
    <td align="right">1.85</td>
    <td align="right">1.85</td>
    <td align="right">1.85</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">15.04</td>
    <td align="right">9.17</td>
    <td align="right">9.14</td>
    <td align="right">9.15</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">1.81</td>
    <td align="right">2.11</td>
    <td align="right">2.11</td>
    <td align="right">2.11</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">1.80</td>
    <td align="right">1.61</td>
    <td align="right">1.61</td>
    <td align="right">1.61</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.24</td>
    <td align="right">2.78</td>
    <td align="right">9.29</td>
    <td align="right">7.45</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.27</td>
    <td align="right">2.78</td>
    <td align="right">8.76</td>
    <td align="right">7.21</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.01</td>
    <td align="right">1.72</td>
    <td align="right">1.71</td>
    <td align="right">1.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.19</td>
    <td align="right">4.12</td>
    <td align="right">10.65</td>
    <td align="right">8.91</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.83</td>
    <td align="right">3.77</td>
    <td align="right">9.51</td>
    <td align="right">8.05</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.51</td>
    <td align="right">1.52</td>
    <td align="right">1.52</td>
    <td align="right">1.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.07</td>
    <td align="right">5.08</td>
    <td align="right">10.63</td>
    <td align="right">9.46</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.06</td>
    <td align="right">5.02</td>
    <td align="right">9.83</td>
    <td align="right">9.17</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.93</td>
    <td align="right">2.42</td>
    <td align="right">1.75</td>
    <td align="right">11.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.49</td>
    <td align="right">5.79</td>
    <td align="right">10.27</td>
    <td align="right">9.75</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.78</td>
    <td align="right">6.08</td>
    <td align="right">10.22</td>
    <td align="right">9.90</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">2.93</td>
    <td align="right">2.94</td>
    <td align="right">1.71</td>
    <td align="right">11.49</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.23</td>
    <td align="right">1.83</td>
    <td align="right">1.83</td>
    <td align="right">1.83</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.32</td>
    <td align="right">1.86</td>
    <td align="right">1.86</td>
    <td align="right">1.90</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.02</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
    <td align="right">1.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.17</td>
    <td align="right">1.87</td>
    <td align="right">1.87</td>
    <td align="right">1.87</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.79</td>
    <td align="right">2.17</td>
    <td align="right">2.17</td>
    <td align="right">2.18</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">1.52</td>
    <td align="right">1.52</td>
    <td align="right">1.52</td>
    <td align="right">1.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.05</td>
    <td align="right">2.96</td>
    <td align="right">2.98</td>
    <td align="right">3.05</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.08</td>
    <td align="right">3.11</td>
    <td align="right">3.10</td>
    <td align="right">3.09</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">2.91</td>
    <td align="right">2.39</td>
    <td align="right">2.39</td>
    <td align="right">2.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.66</td>
    <td align="right">3.42</td>
    <td align="right">3.42</td>
    <td align="right">3.41</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.80</td>
    <td align="right">3.61</td>
    <td align="right">3.64</td>
    <td align="right">3.68</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">3.02</td>
    <td align="right">2.96</td>
    <td align="right">2.95</td>
    <td align="right">2.95</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.04</td>
    <td align="right">1.73</td>
    <td align="right">1.72</td>
    <td align="right">1.71</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.25</td>
    <td align="right">2.79</td>
    <td align="right">9.33</td>
    <td align="right">7.50</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.29</td>
    <td align="right">2.80</td>
    <td align="right">8.81</td>
    <td align="right">7.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.09</td>
    <td align="right">1.66</td>
    <td align="right">1.64</td>
    <td align="right">1.64</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.20</td>
    <td align="right">4.14</td>
    <td align="right">10.68</td>
    <td align="right">8.97</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.79</td>
    <td align="right">3.80</td>
    <td align="right">9.52</td>
    <td align="right">8.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.92</td>
    <td align="right">2.39</td>
    <td align="right">1.74</td>
    <td align="right">11.50</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.09</td>
    <td align="right">5.09</td>
    <td align="right">10.62</td>
    <td align="right">9.41</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.04</td>
    <td align="right">5.00</td>
    <td align="right">9.85</td>
    <td align="right">9.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.97</td>
    <td align="right">2.89</td>
    <td align="right">1.70</td>
    <td align="right">11.48</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.55</td>
    <td align="right">5.82</td>
    <td align="right">10.28</td>
    <td align="right">9.76</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.79</td>
    <td align="right">6.08</td>
    <td align="right">10.25</td>
    <td align="right">9.95</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">1.99</td>
    <td align="right">1.71</td>
    <td align="right">1.71</td>
    <td align="right">1.70</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">2.24</td>
    <td align="right">1.84</td>
    <td align="right">1.84</td>
    <td align="right">1.84</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">2.27</td>
    <td align="right">1.92</td>
    <td align="right">1.87</td>
    <td align="right">1.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">2.06</td>
    <td align="right">1.62</td>
    <td align="right">1.63</td>
    <td align="right">1.62</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">2.18</td>
    <td align="right">1.89</td>
    <td align="right">1.88</td>
    <td align="right">1.89</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">2.81</td>
    <td align="right">2.18</td>
    <td align="right">2.26</td>
    <td align="right">2.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">2.88</td>
    <td align="right">2.38</td>
    <td align="right">2.36</td>
    <td align="right">2.38</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">4.09</td>
    <td align="right">3.00</td>
    <td align="right">2.99</td>
    <td align="right">2.98</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">4.07</td>
    <td align="right">3.08</td>
    <td align="right">3.09</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">2.94</td>
    <td align="right">2.86</td>
    <td align="right">2.85</td>
    <td align="right">2.85</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">4.61</td>
    <td align="right">3.38</td>
    <td align="right">3.41</td>
    <td align="right">3.39</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">4.77</td>
    <td align="right">3.62</td>
    <td align="right">3.62</td>
    <td align="right">3.62</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.22</td>
    <td align="right">3.44</td>
    <td align="right">10.17</td>
    <td align="right">8.39</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">7.00</td>
    <td align="right">3.91</td>
    <td align="right">12.64</td>
    <td align="right">9.24</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">7.68</td>
    <td align="right">5.33</td>
    <td align="right">13.03</td>
    <td align="right">9.98</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.36</td>
    <td align="right">4.58</td>
    <td align="right">9.77</td>
    <td align="right">9.42</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.36</td>
    <td align="right">4.63</td>
    <td align="right">10.23</td>
    <td align="right">10.29</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">10.91</td>
    <td align="right">7.32</td>
    <td align="right">13.53</td>
    <td align="right">11.80</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.52</td>
    <td align="right">5.43</td>
    <td align="right">9.64</td>
    <td align="right">9.85</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.56</td>
    <td align="right">5.90</td>
    <td align="right">11.21</td>
    <td align="right">11.23</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">12.18</td>
    <td align="right">8.07</td>
    <td align="right">12.47</td>
    <td align="right">12.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">7.03</td>
    <td align="right">6.63</td>
    <td align="right">10.28</td>
    <td align="right">10.70</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.47</td>
    <td align="right">6.43</td>
    <td align="right">10.78</td>
    <td align="right">11.93</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">17.28</td>
    <td align="right">11.06</td>
    <td align="right">14.56</td>
    <td align="right">14.13</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">3.22</td>
    <td align="right">3.04</td>
    <td align="right">3.04</td>
    <td align="right">3.04</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">6.95</td>
    <td align="right">3.90</td>
    <td align="right">3.93</td>
    <td align="right">3.90</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">7.71</td>
    <td align="right">4.95</td>
    <td align="right">4.93</td>
    <td align="right">4.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">4.36</td>
    <td align="right">4.02</td>
    <td align="right">4.01</td>
    <td align="right">4.02</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">7.39</td>
    <td align="right">4.33</td>
    <td align="right">4.33</td>
    <td align="right">4.33</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">10.88</td>
    <td align="right">6.91</td>
    <td align="right">6.91</td>
    <td align="right">6.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">5.51</td>
    <td align="right">4.75</td>
    <td align="right">4.74</td>
    <td align="right">4.76</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">8.54</td>
    <td align="right">5.38</td>
    <td align="right">5.36</td>
    <td align="right">5.38</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">12.09</td>
    <td align="right">7.68</td>
    <td align="right">7.68</td>
    <td align="right">7.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">7.02</td>
    <td align="right">5.95</td>
    <td align="right">5.95</td>
    <td align="right">5.94</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">9.40</td>
    <td align="right">6.09</td>
    <td align="right">6.08</td>
    <td align="right">6.04</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">17.10</td>
    <td align="right">10.64</td>
    <td align="right">10.64</td>
    <td align="right">10.64</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">23.80</td>
    <td align="right">11.54</td>
    <td align="right">5.48</td>
    <td align="right">15.44</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">7.79</td>
    <td align="right">6.48</td>
    <td align="right">12.96</td>
    <td align="right">10.59</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.12</td>
    <td align="right">2.38</td>
    <td align="right">2.41</td>
    <td align="right">2.39</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.18</td>
    <td align="right">2.33</td>
    <td align="right">2.33</td>
    <td align="right">2.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">13.07</td>
    <td align="right">11.54</td>
    <td align="right">16.09</td>
    <td align="right">14.98</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.38</td>
    <td align="right">4.14</td>
    <td align="right">4.01</td>
    <td align="right">4.01</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.35</td>
    <td align="right">3.67</td>
    <td align="right">3.69</td>
    <td align="right">3.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">30.45</td>
    <td align="right">24.79</td>
    <td align="right">17.84</td>
    <td align="right">22.66</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">6.74</td>
    <td align="right">6.91</td>
    <td align="right">6.93</td>
    <td align="right">6.83</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.23</td>
    <td align="right">6.34</td>
    <td align="right">6.34</td>
    <td align="right">6.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">53.84</td>
    <td align="right">41.10</td>
    <td align="right">20.14</td>
    <td align="right">31.55</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">9.41</td>
    <td align="right">9.06</td>
    <td align="right">8.65</td>
    <td align="right">8.92</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">7.58</td>
    <td align="right">6.97</td>
    <td align="right">7.29</td>
    <td align="right">6.98</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">7.76</td>
    <td align="right">6.78</td>
    <td align="right">6.75</td>
    <td align="right">6.75</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">2.13</td>
    <td align="right">2.39</td>
    <td align="right">2.41</td>
    <td align="right">2.39</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">2.16</td>
    <td align="right">2.32</td>
    <td align="right">2.35</td>
    <td align="right">2.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">14.07</td>
    <td align="right">12.78</td>
    <td align="right">12.94</td>
    <td align="right">12.37</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">3.28</td>
    <td align="right">4.07</td>
    <td align="right">4.20</td>
    <td align="right">4.32</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">3.43</td>
    <td align="right">3.62</td>
    <td align="right">3.63</td>
    <td align="right">3.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">31.36</td>
    <td align="right">24.86</td>
    <td align="right">25.55</td>
    <td align="right">27.92</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">7.01</td>
    <td align="right">7.19</td>
    <td align="right">7.28</td>
    <td align="right">7.15</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">6.56</td>
    <td align="right">6.89</td>
    <td align="right">7.14</td>
    <td align="right">6.89</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">54.89</td>
    <td align="right">45.11</td>
    <td align="right">47.03</td>
    <td align="right">46.03</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">9.12</td>
    <td align="right">9.05</td>
    <td align="right">8.95</td>
    <td align="right">8.84</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">7.71</td>
    <td align="right">6.59</td>
    <td align="right">6.95</td>
    <td align="right">7.12</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.75</td>
    <td align="right">3.72</td>
    <td align="right">10.14</td>
    <td align="right">8.56</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.72</td>
    <td align="right">3.75</td>
    <td align="right">9.73</td>
    <td align="right">8.40</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.44</td>
    <td align="right">2.70</td>
    <td align="right">2.76</td>
    <td align="right">2.74</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">4.32</td>
    <td align="right">7.77</td>
    <td align="right">14.02</td>
    <td align="right">13.31</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.62</td>
    <td align="right">7.21</td>
    <td align="right">12.04</td>
    <td align="right">11.63</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.98</td>
    <td align="right">3.68</td>
    <td align="right">4.20</td>
    <td align="right">3.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">10.91</td>
    <td align="right">14.15</td>
    <td align="right">15.67</td>
    <td align="right">17.13</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">11.41</td>
    <td align="right">14.52</td>
    <td align="right">14.65</td>
    <td align="right">16.87</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">8.30</td>
    <td align="right">8.13</td>
    <td align="right">5.69</td>
    <td align="right">15.40</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">16.29</td>
    <td align="right">18.73</td>
    <td align="right">15.96</td>
    <td align="right">20.12</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.75</td>
    <td align="right">18.23</td>
    <td align="right">15.66</td>
    <td align="right">20.27</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.40</td>
    <td align="right">10.16</td>
    <td align="right">5.71</td>
    <td align="right">16.11</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.71</td>
    <td align="right">2.75</td>
    <td align="right">2.81</td>
    <td align="right">2.76</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.72</td>
    <td align="right">2.79</td>
    <td align="right">2.84</td>
    <td align="right">2.79</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">2.39</td>
    <td align="right">2.66</td>
    <td align="right">2.69</td>
    <td align="right">2.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.72</td>
    <td align="right">4.14</td>
    <td align="right">4.13</td>
    <td align="right">4.10</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.15</td>
    <td align="right">4.81</td>
    <td align="right">4.67</td>
    <td align="right">4.65</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">2.64</td>
    <td align="right">3.55</td>
    <td align="right">3.48</td>
    <td align="right">3.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.55</td>
    <td align="right">9.05</td>
    <td align="right">9.08</td>
    <td align="right">9.05</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.56</td>
    <td align="right">9.17</td>
    <td align="right">9.21</td>
    <td align="right">9.17</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">7.35</td>
    <td align="right">7.53</td>
    <td align="right">7.57</td>
    <td align="right">7.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.22</td>
    <td align="right">12.15</td>
    <td align="right">12.15</td>
    <td align="right">12.13</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.73</td>
    <td align="right">12.76</td>
    <td align="right">12.78</td>
    <td align="right">12.77</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">9.37</td>
    <td align="right">10.35</td>
    <td align="right">10.30</td>
    <td align="right">10.30</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.37</td>
    <td align="right">2.65</td>
    <td align="right">2.67</td>
    <td align="right">2.65</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.70</td>
    <td align="right">3.67</td>
    <td align="right">10.06</td>
    <td align="right">8.54</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.72</td>
    <td align="right">3.70</td>
    <td align="right">9.54</td>
    <td align="right">8.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.88</td>
    <td align="right">3.30</td>
    <td align="right">3.25</td>
    <td align="right">3.25</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.74</td>
    <td align="right">6.94</td>
    <td align="right">13.05</td>
    <td align="right">12.23</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.14</td>
    <td align="right">6.86</td>
    <td align="right">11.54</td>
    <td align="right">11.24</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.35</td>
    <td align="right">7.52</td>
    <td align="right">4.95</td>
    <td align="right">14.22</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.57</td>
    <td align="right">12.79</td>
    <td align="right">14.59</td>
    <td align="right">15.78</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.56</td>
    <td align="right">12.71</td>
    <td align="right">13.75</td>
    <td align="right">15.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.50</td>
    <td align="right">10.21</td>
    <td align="right">5.72</td>
    <td align="right">15.81</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.19</td>
    <td align="right">17.12</td>
    <td align="right">15.32</td>
    <td align="right">19.39</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.74</td>
    <td align="right">18.25</td>
    <td align="right">15.64</td>
    <td align="right">20.26</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">2.37</td>
    <td align="right">2.64</td>
    <td align="right">2.68</td>
    <td align="right">2.64</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">2.70</td>
    <td align="right">2.76</td>
    <td align="right">2.81</td>
    <td align="right">2.76</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">2.72</td>
    <td align="right">2.78</td>
    <td align="right">2.83</td>
    <td align="right">2.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">2.89</td>
    <td align="right">3.30</td>
    <td align="right">3.35</td>
    <td align="right">3.38</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">3.73</td>
    <td align="right">4.10</td>
    <td align="right">4.13</td>
    <td align="right">4.10</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">4.17</td>
    <td align="right">4.82</td>
    <td align="right">4.67</td>
    <td align="right">4.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">7.40</td>
    <td align="right">7.52</td>
    <td align="right">7.59</td>
    <td align="right">7.52</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">9.53</td>
    <td align="right">9.06</td>
    <td align="right">9.04</td>
    <td align="right">9.05</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">9.52</td>
    <td align="right">9.16</td>
    <td align="right">9.17</td>
    <td align="right">9.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">9.49</td>
    <td align="right">10.40</td>
    <td align="right">10.37</td>
    <td align="right">10.36</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">14.25</td>
    <td align="right">12.14</td>
    <td align="right">12.16</td>
    <td align="right">12.14</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">14.75</td>
    <td align="right">12.76</td>
    <td align="right">12.77</td>
    <td align="right">12.76</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.65</td>
    <td align="right">4.52</td>
    <td align="right">11.27</td>
    <td align="right">9.81</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.85</td>
    <td align="right">4.99</td>
    <td align="right">13.54</td>
    <td align="right">10.57</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">9.02</td>
    <td align="right">7.02</td>
    <td align="right">14.62</td>
    <td align="right">11.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">8.13</td>
    <td align="right">7.55</td>
    <td align="right">11.99</td>
    <td align="right">12.88</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">12.38</td>
    <td align="right">7.97</td>
    <td align="right">12.41</td>
    <td align="right">13.69</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">14.20</td>
    <td align="right">11.54</td>
    <td align="right">17.46</td>
    <td align="right">15.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.18</td>
    <td align="right">12.44</td>
    <td align="right">13.34</td>
    <td align="right">16.39</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">20.92</td>
    <td align="right">14.28</td>
    <td align="right">15.65</td>
    <td align="right">18.77</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">23.17</td>
    <td align="right">18.91</td>
    <td align="right">18.04</td>
    <td align="right">20.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.50</td>
    <td align="right">16.34</td>
    <td align="right">14.99</td>
    <td align="right">19.95</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.14</td>
    <td align="right">19.11</td>
    <td align="right">16.43</td>
    <td align="right">22.78</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">45.66</td>
    <td align="right">34.89</td>
    <td align="right">26.55</td>
    <td align="right">31.84</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">4.64</td>
    <td align="right">4.42</td>
    <td align="right">4.62</td>
    <td align="right">4.43</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">8.85</td>
    <td align="right">5.30</td>
    <td align="right">5.48</td>
    <td align="right">5.28</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">9.02</td>
    <td align="right">7.05</td>
    <td align="right">7.07</td>
    <td align="right">7.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">8.13</td>
    <td align="right">7.85</td>
    <td align="right">7.88</td>
    <td align="right">7.95</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">12.38</td>
    <td align="right">8.14</td>
    <td align="right">8.14</td>
    <td align="right">8.14</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">14.20</td>
    <td align="right">12.10</td>
    <td align="right">12.02</td>
    <td align="right">11.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">14.11</td>
    <td align="right">13.18</td>
    <td align="right">13.21</td>
    <td align="right">13.14</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">20.75</td>
    <td align="right">15.19</td>
    <td align="right">15.13</td>
    <td align="right">15.18</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">23.09</td>
    <td align="right">20.25</td>
    <td align="right">20.16</td>
    <td align="right">20.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">20.53</td>
    <td align="right">17.81</td>
    <td align="right">17.88</td>
    <td align="right">17.80</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">27.21</td>
    <td align="right">20.69</td>
    <td align="right">20.67</td>
    <td align="right">20.67</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">45.73</td>
    <td align="right">35.70</td>
    <td align="right">35.68</td>
    <td align="right">35.72</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.41</td>
    <td align="right">4.98</td>
    <td align="right">3.42</td>
    <td align="right">10.07</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.29</td>
    <td align="right">11.56</td>
    <td align="right">14.60</td>
    <td align="right">14.30</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.81</td>
    <td align="right">3.79</td>
    <td align="right">3.98</td>
    <td align="right">8.53</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.36</td>
    <td align="right">4.13</td>
    <td align="right">4.35</td>
    <td align="right">8.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">15.16</td>
    <td align="right">16.36</td>
    <td align="right">15.15</td>
    <td align="right">17.30</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.43</td>
    <td align="right">4.20</td>
    <td align="right">4.17</td>
    <td align="right">9.07</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.01</td>
    <td align="right">4.50</td>
    <td align="right">4.46</td>
    <td align="right">9.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">20.95</td>
    <td align="right">20.47</td>
    <td align="right">14.33</td>
    <td align="right">19.74</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.07</td>
    <td align="right">4.55</td>
    <td align="right">4.44</td>
    <td align="right">9.51</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.67</td>
    <td align="right">4.89</td>
    <td align="right">4.78</td>
    <td align="right">9.67</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">22.90</td>
    <td align="right">25.40</td>
    <td align="right">14.60</td>
    <td align="right">22.35</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.74</td>
    <td align="right">4.95</td>
    <td align="right">4.82</td>
    <td align="right">10.04</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.29</td>
    <td align="right">5.27</td>
    <td align="right">5.17</td>
    <td align="right">10.27</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1303</td>
    <td align="right">10.31</td>
    <td align="right">12.89</td>
    <td align="right">12.99</td>
    <td align="right">18.15</td>
    <td align="center">4</td>
    <td align="right">3.3706</td>
    <td align="right">3.84</td>
    <td align="right">3.80</td>
    <td align="right">3.99</td>
    <td align="right">8.42</td>
    <td align="center">5</td>
    <td align="right">3.0229</td>
    <td align="right">4.35</td>
    <td align="right">4.12</td>
    <td align="right">4.32</td>
    <td align="right">8.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3077</td>
    <td align="right">18.15</td>
    <td align="right">18.92</td>
    <td align="right">18.80</td>
    <td align="right">24.40</td>
    <td align="center">5</td>
    <td align="right">1.0495</td>
    <td align="right">4.42</td>
    <td align="right">4.19</td>
    <td align="right">4.15</td>
    <td align="right">9.09</td>
    <td align="center">6</td>
    <td align="right">0.8320</td>
    <td align="right">5.06</td>
    <td align="right">4.51</td>
    <td align="right">4.49</td>
    <td align="right">9.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0447</td>
    <td align="right">18.26</td>
    <td align="right">22.94</td>
    <td align="right">22.72</td>
    <td align="right">27.94</td>
    <td align="center">6</td>
    <td align="right">0.4212</td>
    <td align="right">5.08</td>
    <td align="right">4.55</td>
    <td align="right">4.46</td>
    <td align="right">9.57</td>
    <td align="center">7</td>
    <td align="right">0.2916</td>
    <td align="right">5.68</td>
    <td align="right">4.90</td>
    <td align="right">4.80</td>
    <td align="right">9.80</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0063</td>
    <td align="right">23.01</td>
    <td align="right">66.49</td>
    <td align="right">57.37</td>
    <td align="right">70.27</td>
    <td align="center">7</td>
    <td align="right">0.1954</td>
    <td align="right">5.73</td>
    <td align="right">4.93</td>
    <td align="right">4.80</td>
    <td align="right">10.06</td>
    <td align="center">8</td>
    <td align="right">0.1209</td>
    <td align="right">6.32</td>
    <td align="right">11.77</td>
    <td align="right">11.64</td>
    <td align="right">16.94</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.41</td>
    <td align="right">7.03</td>
    <td align="right">11.41</td>
    <td align="right">10.91</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">8.36</td>
    <td align="right">7.56</td>
    <td align="right">12.24</td>
    <td align="right">11.65</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.86</td>
    <td align="right">2.52</td>
    <td align="right">2.84</td>
    <td align="right">8.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.30</td>
    <td align="right">9.82</td>
    <td align="right">12.03</td>
    <td align="right">12.55</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">13.76</td>
    <td align="right">11.31</td>
    <td align="right">13.14</td>
    <td align="right">14.16</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.75</td>
    <td align="right">3.37</td>
    <td align="right">2.60</td>
    <td align="right">9.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.58</td>
    <td align="right">12.92</td>
    <td align="right">14.07</td>
    <td align="right">15.32</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.32</td>
    <td align="right">13.99</td>
    <td align="right">15.47</td>
    <td align="right">16.62</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.28</td>
    <td align="right">4.85</td>
    <td align="right">3.47</td>
    <td align="right">11.66</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">12.25</td>
    <td align="right">14.24</td>
    <td align="right">13.82</td>
    <td align="right">16.96</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">13.79</td>
    <td align="right">19.77</td>
    <td align="right">15.81</td>
    <td align="right">20.91</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.31</td>
    <td align="right">4.89</td>
    <td align="right">3.46</td>
    <td align="right">11.68</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4608</td>
    <td align="right">5.40</td>
    <td align="right">4.98</td>
    <td align="right">5.05</td>
    <td align="right">9.58</td>
    <td align="center">5</td>
    <td align="right">2.2909</td>
    <td align="right">8.38</td>
    <td align="right">5.44</td>
    <td align="right">5.46</td>
    <td align="right">11.00</td>
    <td align="center">5</td>
    <td align="right">2.7470</td>
    <td align="right">2.86</td>
    <td align="right">2.64</td>
    <td align="right">2.89</td>
    <td align="right">8.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4110</td>
    <td align="right">8.27</td>
    <td align="right">7.47</td>
    <td align="right">6.91</td>
    <td align="right">11.92</td>
    <td align="center">8</td>
    <td align="right">0.3808</td>
    <td align="right">12.72</td>
    <td align="right">7.65</td>
    <td align="right">7.41</td>
    <td align="right">13.04</td>
    <td align="center">8</td>
    <td align="right">0.5416</td>
    <td align="right">2.82</td>
    <td align="right">2.56</td>
    <td align="right">2.46</td>
    <td align="right">8.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0737</td>
    <td align="right">10.52</td>
    <td align="right">9.12</td>
    <td align="right">8.94</td>
    <td align="right">13.98</td>
    <td align="center">11</td>
    <td align="right">0.0614</td>
    <td align="right">12.43</td>
    <td align="right">10.78</td>
    <td align="right">10.26</td>
    <td align="right">15.68</td>
    <td align="center">11</td>
    <td align="right">0.1157</td>
    <td align="right">4.30</td>
    <td align="right">3.85</td>
    <td align="right">3.70</td>
    <td align="right">10.45</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0152</td>
    <td align="right">11.65</td>
    <td align="right">10.31</td>
    <td align="right">10.14</td>
    <td align="right">15.20</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">15.17</td>
    <td align="right">12.24</td>
    <td align="right">12.09</td>
    <td align="right">17.38</td>
    <td align="center">13</td>
    <td align="right">0.0268</td>
    <td align="right">4.34</td>
    <td align="right">3.90</td>
    <td align="right">3.72</td>
    <td align="right">10.52</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.80</td>
    <td align="right">2.40</td>
    <td align="right">2.71</td>
    <td align="right">8.88</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.73</td>
    <td align="right">3.56</td>
    <td align="right">3.77</td>
    <td align="right">10.48</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.79</td>
    <td align="right">3.40</td>
    <td align="right">3.65</td>
    <td align="right">10.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.27</td>
    <td align="right">3.85</td>
    <td align="right">3.00</td>
    <td align="right">9.86</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.18</td>
    <td align="right">4.23</td>
    <td align="right">3.48</td>
    <td align="right">10.51</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.72</td>
    <td align="right">4.81</td>
    <td align="right">4.05</td>
    <td align="right">11.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.37</td>
    <td align="right">4.57</td>
    <td align="right">3.11</td>
    <td align="right">10.83</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">7.96</td>
    <td align="right">6.65</td>
    <td align="right">5.23</td>
    <td align="right">13.39</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.74</td>
    <td align="right">6.49</td>
    <td align="right">5.09</td>
    <td align="right">13.05</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.41</td>
    <td align="right">4.65</td>
    <td align="right">3.14</td>
    <td align="right">10.90</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.88</td>
    <td align="right">7.59</td>
    <td align="right">5.30</td>
    <td align="right">13.87</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.02</td>
    <td align="right">7.26</td>
    <td align="right">5.11</td>
    <td align="right">13.43</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4821</td>
    <td align="right">2.81</td>
    <td align="right">2.51</td>
    <td align="right">2.69</td>
    <td align="right">8.66</td>
    <td align="center">5</td>
    <td align="right">2.4383</td>
    <td align="right">3.71</td>
    <td align="right">3.56</td>
    <td align="right">3.81</td>
    <td align="right">10.43</td>
    <td align="center">5</td>
    <td align="right">2.2971</td>
    <td align="right">3.78</td>
    <td align="right">3.47</td>
    <td align="right">3.69</td>
    <td align="right">10.31</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4308</td>
    <td align="right">3.26</td>
    <td align="right">2.60</td>
    <td align="right">2.46</td>
    <td align="right">8.58</td>
    <td align="center">8</td>
    <td align="right">0.4183</td>
    <td align="right">4.16</td>
    <td align="right">4.71</td>
    <td align="right">4.50</td>
    <td align="right">11.01</td>
    <td align="center">8</td>
    <td align="right">0.3720</td>
    <td align="right">5.70</td>
    <td align="right">5.45</td>
    <td align="right">5.35</td>
    <td align="right">12.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0894</td>
    <td align="right">4.37</td>
    <td align="right">3.70</td>
    <td align="right">3.49</td>
    <td align="right">10.10</td>
    <td align="center">11</td>
    <td align="right">0.0788</td>
    <td align="right">8.06</td>
    <td align="right">7.22</td>
    <td align="right">6.95</td>
    <td align="right">14.09</td>
    <td align="center">11</td>
    <td align="right">0.0680</td>
    <td align="right">7.72</td>
    <td align="right">6.79</td>
    <td align="right">6.61</td>
    <td align="right">13.49</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">4.87</td>
    <td align="right">3.75</td>
    <td align="right">3.53</td>
    <td align="right">10.52</td>
    <td align="center">13</td>
    <td align="right">0.0136</td>
    <td align="right">7.90</td>
    <td align="right">14.00</td>
    <td align="right">13.74</td>
    <td align="right">20.03</td>
    <td align="center">14</td>
    <td align="right">0.0150</td>
    <td align="right">8.06</td>
    <td align="right">7.78</td>
    <td align="right">7.46</td>
    <td align="right">14.69</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.11</td>
    <td align="right">6.95</td>
    <td align="right">11.24</td>
    <td align="right">10.82</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">10.02</td>
    <td align="right">9.81</td>
    <td align="right">14.24</td>
    <td align="right">13.11</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.12</td>
    <td align="right">12.43</td>
    <td align="right">16.30</td>
    <td align="right">14.84</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.46</td>
    <td align="right">10.15</td>
    <td align="right">12.37</td>
    <td align="right">13.32</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.73</td>
    <td align="right">11.19</td>
    <td align="right">13.35</td>
    <td align="right">14.47</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.70</td>
    <td align="right">16.13</td>
    <td align="right">16.34</td>
    <td align="right">17.20</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.46</td>
    <td align="right">11.71</td>
    <td align="right">12.05</td>
    <td align="right">14.48</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.30</td>
    <td align="right">13.19</td>
    <td align="right">12.94</td>
    <td align="right">15.68</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.60</td>
    <td align="right">18.27</td>
    <td align="right">18.03</td>
    <td align="right">19.82</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.80</td>
    <td align="right">14.19</td>
    <td align="right">12.35</td>
    <td align="right">16.51</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.48</td>
    <td align="right">15.44</td>
    <td align="right">12.54</td>
    <td align="right">17.24</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.29</td>
    <td align="right">24.17</td>
    <td align="right">19.40</td>
    <td align="right">22.39</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3151</td>
    <td align="right">7.09</td>
    <td align="right">6.39</td>
    <td align="right">6.14</td>
    <td align="right">10.99</td>
    <td align="center">6</td>
    <td align="right">2.3015</td>
    <td align="right">9.91</td>
    <td align="right">7.86</td>
    <td align="right">7.98</td>
    <td align="right">12.97</td>
    <td align="center">7</td>
    <td align="right">2.3446</td>
    <td align="right">10.11</td>
    <td align="right">9.08</td>
    <td align="right">9.25</td>
    <td align="right">14.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4171</td>
    <td align="right">9.44</td>
    <td align="right">8.25</td>
    <td align="right">7.94</td>
    <td align="right">12.90</td>
    <td align="center">7</td>
    <td align="right">0.3864</td>
    <td align="right">11.82</td>
    <td align="right">9.95</td>
    <td align="right">9.43</td>
    <td align="right">15.02</td>
    <td align="center">10</td>
    <td align="right">0.3486</td>
    <td align="right">13.83</td>
    <td align="right">12.99</td>
    <td align="right">12.81</td>
    <td align="right">17.97</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0818</td>
    <td align="right">11.36</td>
    <td align="right">10.49</td>
    <td align="right">10.39</td>
    <td align="right">14.93</td>
    <td align="center">10</td>
    <td align="right">0.0709</td>
    <td align="right">14.43</td>
    <td align="right">13.42</td>
    <td align="right">13.12</td>
    <td align="right">17.09</td>
    <td align="center">11</td>
    <td align="right">0.0515</td>
    <td align="right">15.74</td>
    <td align="right">15.25</td>
    <td align="right">15.24</td>
    <td align="right">20.27</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0222</td>
    <td align="right">14.73</td>
    <td align="right">13.12</td>
    <td align="right">13.00</td>
    <td align="right">16.90</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">16.48</td>
    <td align="right">14.72</td>
    <td align="right">14.62</td>
    <td align="right">18.17</td>
    <td align="center">15</td>
    <td align="right">0.0062</td>
    <td align="right">23.56</td>
    <td align="right">23.34</td>
    <td align="right">23.00</td>
    <td align="right">27.36</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">43.74</td>
    <td align="right">23.13</td>
    <td align="right">12.15</td>
    <td align="right">27.80</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">11.03</td>
    <td align="right">12.09</td>
    <td align="right">16.05</td>
    <td align="right">15.20</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.22</td>
    <td align="right">4.15</td>
    <td align="right">4.27</td>
    <td align="right">9.40</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.79</td>
    <td align="right">4.46</td>
    <td align="right">4.62</td>
    <td align="right">9.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">20.75</td>
    <td align="right">23.07</td>
    <td align="right">17.36</td>
    <td align="right">22.23</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.40</td>
    <td align="right">6.17</td>
    <td align="right">5.90</td>
    <td align="right">11.18</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">7.16</td>
    <td align="right">6.23</td>
    <td align="right">6.14</td>
    <td align="right">11.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">67.93</td>
    <td align="right">79.93</td>
    <td align="right">26.65</td>
    <td align="right">55.98</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.23</td>
    <td align="right">13.72</td>
    <td align="right">13.44</td>
    <td align="right">17.96</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.14</td>
    <td align="right">15.75</td>
    <td align="right">15.58</td>
    <td align="right">19.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">103.57</td>
    <td align="right">122.39</td>
    <td align="right">32.81</td>
    <td align="right">80.38</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.63</td>
    <td align="right">18.77</td>
    <td align="right">18.32</td>
    <td align="right">22.75</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.85</td>
    <td align="right">19.31</td>
    <td align="right">19.20</td>
    <td align="right">23.36</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1519</td>
    <td align="right">10.94</td>
    <td align="right">13.51</td>
    <td align="right">13.57</td>
    <td align="right">18.95</td>
    <td align="center">4</td>
    <td align="right">3.3467</td>
    <td align="right">4.25</td>
    <td align="right">4.12</td>
    <td align="right">4.25</td>
    <td align="right">9.44</td>
    <td align="center">5</td>
    <td align="right">3.0383</td>
    <td align="right">4.75</td>
    <td align="right">4.43</td>
    <td align="right">4.59</td>
    <td align="right">9.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3180</td>
    <td align="right">24.10</td>
    <td align="right">26.30</td>
    <td align="right">25.89</td>
    <td align="right">31.03</td>
    <td align="center">5</td>
    <td align="right">1.0300</td>
    <td align="right">6.49</td>
    <td align="right">6.16</td>
    <td align="right">5.97</td>
    <td align="right">11.16</td>
    <td align="center">6</td>
    <td align="right">0.8268</td>
    <td align="right">7.34</td>
    <td align="right">6.72</td>
    <td align="right">6.48</td>
    <td align="right">11.29</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0469</td>
    <td align="right">67.37</td>
    <td align="right">84.58</td>
    <td align="right">84.55</td>
    <td align="right">89.21</td>
    <td align="center">6</td>
    <td align="right">0.4034</td>
    <td align="right">15.24</td>
    <td align="right">13.61</td>
    <td align="right">13.44</td>
    <td align="right">17.84</td>
    <td align="center">7</td>
    <td align="right">0.2883</td>
    <td align="right">16.19</td>
    <td align="right">15.33</td>
    <td align="right">15.14</td>
    <td align="right">19.34</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0065</td>
    <td align="right">102.54</td>
    <td align="right">129.39</td>
    <td align="right">129.10</td>
    <td align="right">133.33</td>
    <td align="center">7</td>
    <td align="right">0.1887</td>
    <td align="right">19.91</td>
    <td align="right">19.17</td>
    <td align="right">18.73</td>
    <td align="right">23.17</td>
    <td align="center">8</td>
    <td align="right">0.1194</td>
    <td align="right">20.72</td>
    <td align="right">19.36</td>
    <td align="right">19.29</td>
    <td align="right">23.20</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.12</td>
    <td align="right">7.65</td>
    <td align="right">12.07</td>
    <td align="right">11.78</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">8.62</td>
    <td align="right">8.33</td>
    <td align="right">13.08</td>
    <td align="right">12.35</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.23</td>
    <td align="right">2.82</td>
    <td align="right">3.18</td>
    <td align="right">9.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">10.73</td>
    <td align="right">12.44</td>
    <td align="right">14.00</td>
    <td align="right">15.46</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">16.11</td>
    <td align="right">15.23</td>
    <td align="right">14.46</td>
    <td align="right">17.60</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.98</td>
    <td align="right">5.52</td>
    <td align="right">4.84</td>
    <td align="right">10.98</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">25.82</td>
    <td align="right">29.76</td>
    <td align="right">22.05</td>
    <td align="right">29.20</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">29.50</td>
    <td align="right">31.53</td>
    <td align="right">26.06</td>
    <td align="right">33.14</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">13.89</td>
    <td align="right">15.70</td>
    <td align="right">12.09</td>
    <td align="right">18.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.10</td>
    <td align="right">40.04</td>
    <td align="right">24.87</td>
    <td align="right">38.72</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.96</td>
    <td align="right">58.06</td>
    <td align="right">30.88</td>
    <td align="right">54.06</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.39</td>
    <td align="right">18.33</td>
    <td align="right">13.83</td>
    <td align="right">21.31</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4510</td>
    <td align="right">6.15</td>
    <td align="right">5.51</td>
    <td align="right">5.46</td>
    <td align="right">10.35</td>
    <td align="center">5</td>
    <td align="right">2.3157</td>
    <td align="right">8.66</td>
    <td align="right">5.87</td>
    <td align="right">5.80</td>
    <td align="right">11.79</td>
    <td align="center">5</td>
    <td align="right">2.7361</td>
    <td align="right">3.23</td>
    <td align="right">2.95</td>
    <td align="right">3.22</td>
    <td align="right">9.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4207</td>
    <td align="right">16.28</td>
    <td align="right">15.33</td>
    <td align="right">14.93</td>
    <td align="right">19.80</td>
    <td align="center">8</td>
    <td align="right">0.3724</td>
    <td align="right">15.22</td>
    <td align="right">10.32</td>
    <td align="right">9.84</td>
    <td align="right">16.02</td>
    <td align="center">8</td>
    <td align="right">0.5415</td>
    <td align="right">4.91</td>
    <td align="right">4.53</td>
    <td align="right">4.35</td>
    <td align="right">10.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0764</td>
    <td align="right">25.86</td>
    <td align="right">23.43</td>
    <td align="right">23.32</td>
    <td align="right">27.66</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">29.60</td>
    <td align="right">28.40</td>
    <td align="right">28.43</td>
    <td align="right">33.17</td>
    <td align="center">11</td>
    <td align="right">0.1179</td>
    <td align="right">13.89</td>
    <td align="right">13.36</td>
    <td align="right">13.27</td>
    <td align="right">17.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">36.10</td>
    <td align="right">35.73</td>
    <td align="right">35.44</td>
    <td align="right">39.90</td>
    <td align="center">14</td>
    <td align="right">0.0122</td>
    <td align="right">39.83</td>
    <td align="right">38.01</td>
    <td align="right">38.11</td>
    <td align="right">42.53</td>
    <td align="center">13</td>
    <td align="right">0.0275</td>
    <td align="right">16.39</td>
    <td align="right">15.50</td>
    <td align="right">15.30</td>
    <td align="right">20.27</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.19</td>
    <td align="right">2.69</td>
    <td align="right">2.99</td>
    <td align="right">9.47</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.15</td>
    <td align="right">3.89</td>
    <td align="right">4.05</td>
    <td align="right">11.35</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.23</td>
    <td align="right">3.67</td>
    <td align="right">3.97</td>
    <td align="right">11.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">5.81</td>
    <td align="right">6.16</td>
    <td align="right">5.11</td>
    <td align="right">11.45</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">6.46</td>
    <td align="right">6.69</td>
    <td align="right">5.84</td>
    <td align="right">12.72</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">8.26</td>
    <td align="right">7.88</td>
    <td align="right">6.73</td>
    <td align="right">13.49</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.93</td>
    <td align="right">15.54</td>
    <td align="right">11.77</td>
    <td align="right">17.80</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">22.79</td>
    <td align="right">19.16</td>
    <td align="right">16.11</td>
    <td align="right">22.90</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.60</td>
    <td align="right">18.86</td>
    <td align="right">15.90</td>
    <td align="right">22.09</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">18.15</td>
    <td align="right">18.53</td>
    <td align="right">13.62</td>
    <td align="right">20.79</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.70</td>
    <td align="right">27.63</td>
    <td align="right">19.29</td>
    <td align="right">27.44</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.76</td>
    <td align="right">27.48</td>
    <td align="right">19.15</td>
    <td align="right">27.09</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4788</td>
    <td align="right">3.20</td>
    <td align="right">2.83</td>
    <td align="right">3.02</td>
    <td align="right">9.35</td>
    <td align="center">5</td>
    <td align="right">2.4546</td>
    <td align="right">4.15</td>
    <td align="right">3.83</td>
    <td align="right">4.10</td>
    <td align="right">11.35</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.21</td>
    <td align="right">3.77</td>
    <td align="right">4.01</td>
    <td align="right">11.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4394</td>
    <td align="right">5.78</td>
    <td align="right">5.15</td>
    <td align="right">4.78</td>
    <td align="right">10.37</td>
    <td align="center">8</td>
    <td align="right">0.4210</td>
    <td align="right">6.29</td>
    <td align="right">6.89</td>
    <td align="right">6.31</td>
    <td align="right">12.95</td>
    <td align="center">8</td>
    <td align="right">0.3754</td>
    <td align="right">7.92</td>
    <td align="right">7.82</td>
    <td align="right">7.35</td>
    <td align="right">14.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">14.77</td>
    <td align="right">13.31</td>
    <td align="right">13.18</td>
    <td align="right">17.35</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">22.72</td>
    <td align="right">21.78</td>
    <td align="right">21.31</td>
    <td align="right">26.31</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">20.64</td>
    <td align="right">21.33</td>
    <td align="right">19.44</td>
    <td align="right">24.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0178</td>
    <td align="right">17.72</td>
    <td align="right">15.46</td>
    <td align="right">15.34</td>
    <td align="right">20.01</td>
    <td align="center">13</td>
    <td align="right">0.0160</td>
    <td align="right">28.74</td>
    <td align="right">28.09</td>
    <td align="right">27.97</td>
    <td align="right">32.96</td>
    <td align="center">14</td>
    <td align="right">0.0110</td>
    <td align="right">28.78</td>
    <td align="right">27.95</td>
    <td align="right">27.75</td>
    <td align="right">32.64</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.71</td>
    <td align="right">7.56</td>
    <td align="right">11.95</td>
    <td align="right">11.67</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.53</td>
    <td align="right">10.92</td>
    <td align="right">14.96</td>
    <td align="right">14.20</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.49</td>
    <td align="right">13.91</td>
    <td align="right">17.17</td>
    <td align="right">16.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">11.66</td>
    <td align="right">12.43</td>
    <td align="right">13.94</td>
    <td align="right">15.52</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">15.33</td>
    <td align="right">15.40</td>
    <td align="right">15.77</td>
    <td align="right">18.57</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">16.84</td>
    <td align="right">19.70</td>
    <td align="right">17.82</td>
    <td align="right">20.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">25.09</td>
    <td align="right">25.38</td>
    <td align="right">19.85</td>
    <td align="right">27.41</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.07</td>
    <td align="right">32.03</td>
    <td align="right">20.40</td>
    <td align="right">32.75</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">40.49</td>
    <td align="right">44.11</td>
    <td align="right">27.91</td>
    <td align="right">38.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">35.36</td>
    <td align="right">34.81</td>
    <td align="right">23.20</td>
    <td align="right">36.99</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">42.85</td>
    <td align="right">41.93</td>
    <td align="right">22.82</td>
    <td align="right">42.32</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">68.95</td>
    <td align="right">66.14</td>
    <td align="right">37.33</td>
    <td align="right">55.52</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3292</td>
    <td align="right">7.69</td>
    <td align="right">6.93</td>
    <td align="right">6.50</td>
    <td align="right">11.69</td>
    <td align="center">6</td>
    <td align="right">2.2986</td>
    <td align="right">10.64</td>
    <td align="right">8.46</td>
    <td align="right">8.52</td>
    <td align="right">13.79</td>
    <td align="center">7</td>
    <td align="right">2.3389</td>
    <td align="right">11.43</td>
    <td align="right">10.02</td>
    <td align="right">10.24</td>
    <td align="right">15.62</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">11.67</td>
    <td align="right">10.52</td>
    <td align="right">10.09</td>
    <td align="right">15.45</td>
    <td align="center">7</td>
    <td align="right">0.3845</td>
    <td align="right">14.97</td>
    <td align="right">13.50</td>
    <td align="right">12.19</td>
    <td align="right">18.48</td>
    <td align="center">10</td>
    <td align="right">0.3468</td>
    <td align="right">16.84</td>
    <td align="right">15.83</td>
    <td align="right">15.57</td>
    <td align="right">20.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">25.08</td>
    <td align="right">23.79</td>
    <td align="right">23.77</td>
    <td align="right">28.30</td>
    <td align="center">10</td>
    <td align="right">0.0714</td>
    <td align="right">33.08</td>
    <td align="right">32.44</td>
    <td align="right">32.46</td>
    <td align="right">36.33</td>
    <td align="center">11</td>
    <td align="right">0.0493</td>
    <td align="right">40.58</td>
    <td align="right">39.37</td>
    <td align="right">39.23</td>
    <td align="right">43.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">35.36</td>
    <td align="right">33.77</td>
    <td align="right">33.79</td>
    <td align="right">37.35</td>
    <td align="center">12</td>
    <td align="right">0.0152</td>
    <td align="right">42.88</td>
    <td align="right">41.01</td>
    <td align="right">41.04</td>
    <td align="right">44.31</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">68.91</td>
    <td align="right">65.29</td>
    <td align="right">64.80</td>
    <td align="right">68.82</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">74.37</td>
    <td align="right">14.14</td>
    <td align="right">7.84</td>
    <td align="right">16.90</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">30.93</td>
    <td align="right">43.95</td>
    <td align="right">37.70</td>
    <td align="right">41.11</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.32</td>
    <td align="right">16.00</td>
    <td align="right">16.32</td>
    <td align="right">23.56</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.56</td>
    <td align="right">17.31</td>
    <td align="right">17.82</td>
    <td align="right">24.59</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.95</td>
    <td align="right">66.97</td>
    <td align="right">40.53</td>
    <td align="right">53.90</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.29</td>
    <td align="right">18.00</td>
    <td align="right">18.18</td>
    <td align="right">26.11</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.04</td>
    <td align="right">18.95</td>
    <td align="right">18.65</td>
    <td align="right">26.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">56.93</td>
    <td align="right">82.00</td>
    <td align="right">39.10</td>
    <td align="right">61.21</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.37</td>
    <td align="right">19.99</td>
    <td align="right">19.65</td>
    <td align="right">29.01</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">17.11</td>
    <td align="right">21.29</td>
    <td align="right">20.51</td>
    <td align="right">28.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">73.12</td>
    <td align="right">100.43</td>
    <td align="right">41.10</td>
    <td align="right">70.73</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.66</td>
    <td align="right">21.68</td>
    <td align="right">21.83</td>
    <td align="right">30.18</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">19.66</td>
    <td align="right">22.77</td>
    <td align="right">22.52</td>
    <td align="right">30.50</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">30.90</td>
    <td align="right">41.26</td>
    <td align="right">41.09</td>
    <td align="right">49.92</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">13.28</td>
    <td align="right">15.97</td>
    <td align="right">16.48</td>
    <td align="right">23.81</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">14.61</td>
    <td align="right">17.67</td>
    <td align="right">17.59</td>
    <td align="right">25.35</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">46.67</td>
    <td align="right">59.79</td>
    <td align="right">59.16</td>
    <td align="right">68.81</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">15.28</td>
    <td align="right">18.17</td>
    <td align="right">18.18</td>
    <td align="right">26.13</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">16.05</td>
    <td align="right">18.96</td>
    <td align="right">19.78</td>
    <td align="right">26.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">56.48</td>
    <td align="right">70.20</td>
    <td align="right">70.39</td>
    <td align="right">79.50</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">16.38</td>
    <td align="right">20.00</td>
    <td align="right">19.52</td>
    <td align="right">28.63</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">16.98</td>
    <td align="right">20.80</td>
    <td align="right">20.45</td>
    <td align="right">28.72</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">72.38</td>
    <td align="right">105.58</td>
    <td align="right">114.35</td>
    <td align="right">115.34</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">17.66</td>
    <td align="right">21.89</td>
    <td align="right">21.78</td>
    <td align="right">30.60</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">18.11</td>
    <td align="right">21.77</td>
    <td align="right">21.53</td>
    <td align="right">30.26</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.72</td>
    <td align="right">23.71</td>
    <td align="right">27.33</td>
    <td align="right">28.82</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.24</td>
    <td align="right">28.07</td>
    <td align="right">29.51</td>
    <td align="right">31.61</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.85</td>
    <td align="right">15.14</td>
    <td align="right">24.27</td>
    <td align="right">21.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.56</td>
    <td align="right">30.52</td>
    <td align="right">28.37</td>
    <td align="right">31.72</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.07</td>
    <td align="right">36.10</td>
    <td align="right">34.05</td>
    <td align="right">35.35</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">14.93</td>
    <td align="right">19.31</td>
    <td align="right">26.14</td>
    <td align="right">25.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.42</td>
    <td align="right">42.98</td>
    <td align="right">31.20</td>
    <td align="right">39.56</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.40</td>
    <td align="right">49.36</td>
    <td align="right">39.97</td>
    <td align="right">44.70</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">17.01</td>
    <td align="right">21.57</td>
    <td align="right">27.17</td>
    <td align="right">27.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.17</td>
    <td align="right">47.71</td>
    <td align="right">29.65</td>
    <td align="right">41.93</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.56</td>
    <td align="right">57.10</td>
    <td align="right">41.97</td>
    <td align="right">49.62</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">24.01</td>
    <td align="right">29.17</td>
    <td align="right">26.99</td>
    <td align="right">30.47</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.67</td>
    <td align="right">23.91</td>
    <td align="right">23.90</td>
    <td align="right">30.53</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.23</td>
    <td align="right">26.79</td>
    <td align="right">26.83</td>
    <td align="right">32.67</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">12.85</td>
    <td align="right">16.30</td>
    <td align="right">16.69</td>
    <td align="right">23.37</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.97</td>
    <td align="right">29.70</td>
    <td align="right">29.77</td>
    <td align="right">33.80</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.08</td>
    <td align="right">35.17</td>
    <td align="right">34.78</td>
    <td align="right">39.50</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">14.86</td>
    <td align="right">18.72</td>
    <td align="right">18.25</td>
    <td align="right">25.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.50</td>
    <td align="right">37.60</td>
    <td align="right">37.41</td>
    <td align="right">41.58</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.63</td>
    <td align="right">49.52</td>
    <td align="right">49.27</td>
    <td align="right">54.23</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">16.94</td>
    <td align="right">21.39</td>
    <td align="right">20.70</td>
    <td align="right">28.31</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.10</td>
    <td align="right">42.05</td>
    <td align="right">41.82</td>
    <td align="right">46.03</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.56</td>
    <td align="right">58.63</td>
    <td align="right">58.34</td>
    <td align="right">63.10</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">24.17</td>
    <td align="right">26.15</td>
    <td align="right">26.07</td>
    <td align="right">32.90</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.44</td>
    <td align="right">16.71</td>
    <td align="right">24.69</td>
    <td align="right">22.78</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.86</td>
    <td align="right">23.69</td>
    <td align="right">27.33</td>
    <td align="right">28.63</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.21</td>
    <td align="right">27.66</td>
    <td align="right">29.48</td>
    <td align="right">31.12</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.02</td>
    <td align="right">19.96</td>
    <td align="right">26.88</td>
    <td align="right">25.73</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.98</td>
    <td align="right">30.53</td>
    <td align="right">28.54</td>
    <td align="right">31.64</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.05</td>
    <td align="right">34.39</td>
    <td align="right">34.04</td>
    <td align="right">35.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.54</td>
    <td align="right">22.87</td>
    <td align="right">28.46</td>
    <td align="right">28.07</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.19</td>
    <td align="right">43.07</td>
    <td align="right">31.14</td>
    <td align="right">39.59</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.45</td>
    <td align="right">49.38</td>
    <td align="right">40.05</td>
    <td align="right">44.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.78</td>
    <td align="right">30.83</td>
    <td align="right">28.59</td>
    <td align="right">32.38</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.16</td>
    <td align="right">47.20</td>
    <td align="right">29.85</td>
    <td align="right">41.94</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.59</td>
    <td align="right">57.20</td>
    <td align="right">42.15</td>
    <td align="right">49.56</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">14.41</td>
    <td align="right">17.25</td>
    <td align="right">17.21</td>
    <td align="right">24.96</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">19.87</td>
    <td align="right">23.90</td>
    <td align="right">23.90</td>
    <td align="right">30.44</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.23</td>
    <td align="right">27.80</td>
    <td align="right">26.84</td>
    <td align="right">32.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">19.03</td>
    <td align="right">21.56</td>
    <td align="right">21.21</td>
    <td align="right">28.45</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">26.58</td>
    <td align="right">29.70</td>
    <td align="right">29.79</td>
    <td align="right">33.88</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">37.06</td>
    <td align="right">35.15</td>
    <td align="right">34.80</td>
    <td align="right">39.51</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">23.53</td>
    <td align="right">24.47</td>
    <td align="right">24.17</td>
    <td align="right">31.19</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.49</td>
    <td align="right">37.63</td>
    <td align="right">37.28</td>
    <td align="right">41.74</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">68.63</td>
    <td align="right">49.57</td>
    <td align="right">49.35</td>
    <td align="right">54.14</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">31.81</td>
    <td align="right">34.29</td>
    <td align="right">33.94</td>
    <td align="right">39.06</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.42</td>
    <td align="right">42.14</td>
    <td align="right">41.71</td>
    <td align="right">46.17</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">82.62</td>
    <td align="right">58.72</td>
    <td align="right">58.35</td>
    <td align="right">63.18</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.34</td>
    <td align="right">24.33</td>
    <td align="right">28.10</td>
    <td align="right">28.23</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.71</td>
    <td align="right">31.71</td>
    <td align="right">36.40</td>
    <td align="right">34.39</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.41</td>
    <td align="right">37.18</td>
    <td align="right">35.03</td>
    <td align="right">36.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.46</td>
    <td align="right">37.56</td>
    <td align="right">28.44</td>
    <td align="right">36.39</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.37</td>
    <td align="right">41.21</td>
    <td align="right">34.63</td>
    <td align="right">39.73</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">42.35</td>
    <td align="right">47.37</td>
    <td align="right">35.11</td>
    <td align="right">41.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.08</td>
    <td align="right">44.14</td>
    <td align="right">28.27</td>
    <td align="right">40.16</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.51</td>
    <td align="right">50.04</td>
    <td align="right">35.89</td>
    <td align="right">44.52</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">44.21</td>
    <td align="right">51.81</td>
    <td align="right">32.14</td>
    <td align="right">44.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.33</td>
    <td align="right">49.79</td>
    <td align="right">29.62</td>
    <td align="right">43.13</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.50</td>
    <td align="right">52.73</td>
    <td align="right">35.64</td>
    <td align="right">46.06</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">61.36</td>
    <td align="right">65.43</td>
    <td align="right">33.28</td>
    <td align="right">52.38</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.32</td>
    <td align="right">24.38</td>
    <td align="right">24.25</td>
    <td align="right">30.03</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">33.75</td>
    <td align="right">32.75</td>
    <td align="right">32.62</td>
    <td align="right">37.48</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">29.20</td>
    <td align="right">35.03</td>
    <td align="right">35.03</td>
    <td align="right">40.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">28.40</td>
    <td align="right">33.89</td>
    <td align="right">33.60</td>
    <td align="right">38.54</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">45.37</td>
    <td align="right">39.97</td>
    <td align="right">39.69</td>
    <td align="right">45.07</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">41.91</td>
    <td align="right">45.13</td>
    <td align="right">44.98</td>
    <td align="right">50.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">37.10</td>
    <td align="right">41.46</td>
    <td align="right">41.02</td>
    <td align="right">46.08</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">49.48</td>
    <td align="right">49.59</td>
    <td align="right">49.23</td>
    <td align="right">54.16</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">43.96</td>
    <td align="right">47.70</td>
    <td align="right">47.29</td>
    <td align="right">53.13</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">42.29</td>
    <td align="right">47.26</td>
    <td align="right">47.01</td>
    <td align="right">51.58</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">52.41</td>
    <td align="right">52.90</td>
    <td align="right">52.66</td>
    <td align="right">57.31</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">62.97</td>
    <td align="right">65.01</td>
    <td align="right">64.52</td>
    <td align="right">71.20</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">107.91</td>
    <td align="right">69.01</td>
    <td align="right">22.51</td>
    <td align="right">55.53</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">42.28</td>
    <td align="right">58.42</td>
    <td align="right">46.24</td>
    <td align="right">52.27</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">16.18</td>
    <td align="right">20.57</td>
    <td align="right">19.08</td>
    <td align="right">26.56</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">15.61</td>
    <td align="right">18.26</td>
    <td align="right">18.73</td>
    <td align="right">28.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">101.18</td>
    <td align="right">131.73</td>
    <td align="right">60.24</td>
    <td align="right">95.89</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.20</td>
    <td align="right">27.66</td>
    <td align="right">27.79</td>
    <td align="right">35.01</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">26.35</td>
    <td align="right">31.30</td>
    <td align="right">29.43</td>
    <td align="right">42.03</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">189.78</td>
    <td align="right">249.37</td>
    <td align="right">78.31</td>
    <td align="right">164.22</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.40</td>
    <td align="right">46.67</td>
    <td align="right">46.46</td>
    <td align="right">57.11</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">38.94</td>
    <td align="right">48.18</td>
    <td align="right">47.85</td>
    <td align="right">57.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">296.55</td>
    <td align="right">400.90</td>
    <td align="right">99.20</td>
    <td align="right">252.65</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">47.92</td>
    <td align="right">63.28</td>
    <td align="right">63.52</td>
    <td align="right">72.23</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">62.84</td>
    <td align="right">63.34</td>
    <td align="right">62.99</td>
    <td align="right">72.69</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">40.01</td>
    <td align="right">50.61</td>
    <td align="right">49.86</td>
    <td align="right">59.20</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.74</td>
    <td align="right">18.89</td>
    <td align="right">18.89</td>
    <td align="right">26.69</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">17.05</td>
    <td align="right">19.97</td>
    <td align="right">20.27</td>
    <td align="right">28.33</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">95.20</td>
    <td align="right">110.21</td>
    <td align="right">105.62</td>
    <td align="right">117.89</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.94</td>
    <td align="right">27.75</td>
    <td align="right">28.19</td>
    <td align="right">35.68</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">26.07</td>
    <td align="right">31.57</td>
    <td align="right">31.66</td>
    <td align="right">40.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">192.70</td>
    <td align="right">179.75</td>
    <td align="right">175.48</td>
    <td align="right">188.80</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.43</td>
    <td align="right">46.84</td>
    <td align="right">46.61</td>
    <td align="right">56.89</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">38.64</td>
    <td align="right">47.15</td>
    <td align="right">46.94</td>
    <td align="right">55.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">295.81</td>
    <td align="right">403.49</td>
    <td align="right">407.64</td>
    <td align="right">410.01</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">46.62</td>
    <td align="right">63.03</td>
    <td align="right">63.34</td>
    <td align="right">72.51</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">59.11</td>
    <td align="right">64.08</td>
    <td align="right">64.11</td>
    <td align="right">73.58</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.31</td>
    <td align="right">27.50</td>
    <td align="right">29.94</td>
    <td align="right">33.09</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.64</td>
    <td align="right">32.58</td>
    <td align="right">31.27</td>
    <td align="right">35.01</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">14.13</td>
    <td align="right">16.41</td>
    <td align="right">26.10</td>
    <td align="right">24.60</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">39.37</td>
    <td align="right">43.82</td>
    <td align="right">37.79</td>
    <td align="right">44.78</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.45</td>
    <td align="right">49.20</td>
    <td align="right">45.75</td>
    <td align="right">50.83</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">23.41</td>
    <td align="right">28.02</td>
    <td align="right">34.22</td>
    <td align="right">33.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.47</td>
    <td align="right">74.85</td>
    <td align="right">48.88</td>
    <td align="right">68.00</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">101.61</td>
    <td align="right">81.77</td>
    <td align="right">66.11</td>
    <td align="right">77.24</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.39</td>
    <td align="right">45.31</td>
    <td align="right">45.78</td>
    <td align="right">47.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.58</td>
    <td align="right">99.98</td>
    <td align="right">57.41</td>
    <td align="right">88.59</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.29</td>
    <td align="right">110.28</td>
    <td align="right">92.71</td>
    <td align="right">103.25</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">69.99</td>
    <td align="right">76.13</td>
    <td align="right">53.68</td>
    <td align="right">73.01</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.64</td>
    <td align="right">27.70</td>
    <td align="right">27.98</td>
    <td align="right">35.15</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.34</td>
    <td align="right">30.18</td>
    <td align="right">29.83</td>
    <td align="right">36.10</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">15.27</td>
    <td align="right">19.07</td>
    <td align="right">20.14</td>
    <td align="right">26.17</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.16</td>
    <td align="right">43.33</td>
    <td align="right">43.31</td>
    <td align="right">47.29</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.56</td>
    <td align="right">53.22</td>
    <td align="right">52.86</td>
    <td align="right">59.08</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">25.09</td>
    <td align="right">28.40</td>
    <td align="right">27.90</td>
    <td align="right">36.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.50</td>
    <td align="right">72.19</td>
    <td align="right">72.10</td>
    <td align="right">76.38</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.90</td>
    <td align="right">82.31</td>
    <td align="right">82.18</td>
    <td align="right">87.24</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">42.25</td>
    <td align="right">45.85</td>
    <td align="right">45.22</td>
    <td align="right">51.96</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.14</td>
    <td align="right">94.89</td>
    <td align="right">94.63</td>
    <td align="right">99.05</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">133.60</td>
    <td align="right">108.08</td>
    <td align="right">107.90</td>
    <td align="right">112.54</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">70.14</td>
    <td align="right">75.26</td>
    <td align="right">75.04</td>
    <td align="right">82.39</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">15.85</td>
    <td align="right">18.46</td>
    <td align="right">28.72</td>
    <td align="right">26.23</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">23.71</td>
    <td align="right">27.97</td>
    <td align="right">30.47</td>
    <td align="right">33.43</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.50</td>
    <td align="right">34.86</td>
    <td align="right">33.32</td>
    <td align="right">37.36</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">30.58</td>
    <td align="right">31.85</td>
    <td align="right">38.65</td>
    <td align="right">38.75</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">39.51</td>
    <td align="right">44.25</td>
    <td align="right">37.46</td>
    <td align="right">45.38</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">54.08</td>
    <td align="right">52.37</td>
    <td align="right">45.64</td>
    <td align="right">52.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.47</td>
    <td align="right">46.54</td>
    <td align="right">50.32</td>
    <td align="right">52.27</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">66.87</td>
    <td align="right">76.27</td>
    <td align="right">50.56</td>
    <td align="right">68.82</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">101.88</td>
    <td align="right">82.24</td>
    <td align="right">66.41</td>
    <td align="right">76.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">81.92</td>
    <td align="right">82.33</td>
    <td align="right">61.06</td>
    <td align="right">79.20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.28</td>
    <td align="right">97.85</td>
    <td align="right">55.50</td>
    <td align="right">85.49</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.07</td>
    <td align="right">109.74</td>
    <td align="right">88.51</td>
    <td align="right">99.93</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">15.57</td>
    <td align="right">19.07</td>
    <td align="right">19.11</td>
    <td align="right">30.05</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">21.98</td>
    <td align="right">26.40</td>
    <td align="right">26.57</td>
    <td align="right">33.96</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.26</td>
    <td align="right">31.69</td>
    <td align="right">31.77</td>
    <td align="right">38.07</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">29.54</td>
    <td align="right">32.35</td>
    <td align="right">31.83</td>
    <td align="right">38.72</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">40.04</td>
    <td align="right">43.84</td>
    <td align="right">44.07</td>
    <td align="right">47.91</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">53.97</td>
    <td align="right">48.77</td>
    <td align="right">48.31</td>
    <td align="right">54.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">48.01</td>
    <td align="right">53.86</td>
    <td align="right">52.90</td>
    <td align="right">60.80</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.77</td>
    <td align="right">73.36</td>
    <td align="right">73.04</td>
    <td align="right">77.62</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">102.65</td>
    <td align="right">82.19</td>
    <td align="right">81.95</td>
    <td align="right">86.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">82.47</td>
    <td align="right">86.86</td>
    <td align="right">86.15</td>
    <td align="right">92.34</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.48</td>
    <td align="right">95.45</td>
    <td align="right">95.20</td>
    <td align="right">99.56</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">134.13</td>
    <td align="right">110.65</td>
    <td align="right">110.54</td>
    <td align="right">114.52</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.20</td>
    <td align="right">28.74</td>
    <td align="right">31.32</td>
    <td align="right">33.30</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">38.13</td>
    <td align="right">39.11</td>
    <td align="right">43.23</td>
    <td align="right">41.45</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">36.85</td>
    <td align="right">45.61</td>
    <td align="right">40.61</td>
    <td align="right">46.06</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">42.09</td>
    <td align="right">52.64</td>
    <td align="right">38.07</td>
    <td align="right">51.40</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">60.68</td>
    <td align="right">56.92</td>
    <td align="right">45.79</td>
    <td align="right">54.78</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">64.33</td>
    <td align="right">71.48</td>
    <td align="right">45.57</td>
    <td align="right">61.74</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">66.04</td>
    <td align="right">71.92</td>
    <td align="right">46.75</td>
    <td align="right">67.58</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">86.46</td>
    <td align="right">87.03</td>
    <td align="right">59.01</td>
    <td align="right">79.02</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">90.19</td>
    <td align="right">93.25</td>
    <td align="right">43.54</td>
    <td align="right">76.79</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">83.96</td>
    <td align="right">89.79</td>
    <td align="right">56.88</td>
    <td align="right">82.97</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">105.71</td>
    <td align="right">104.44</td>
    <td align="right">67.06</td>
    <td align="right">93.65</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">140.64</td>
    <td align="right">144.13</td>
    <td align="right">51.06</td>
    <td align="right">112.75</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.80</td>
    <td align="right">28.73</td>
    <td align="right">28.74</td>
    <td align="right">35.37</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">36.92</td>
    <td align="right">38.02</td>
    <td align="right">37.94</td>
    <td align="right">42.87</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">36.63</td>
    <td align="right">42.59</td>
    <td align="right">41.81</td>
    <td align="right">46.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">40.76</td>
    <td align="right">46.11</td>
    <td align="right">46.01</td>
    <td align="right">50.47</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">58.73</td>
    <td align="right">57.72</td>
    <td align="right">57.32</td>
    <td align="right">64.06</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">62.07</td>
    <td align="right">66.50</td>
    <td align="right">66.26</td>
    <td align="right">71.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">65.38</td>
    <td align="right">68.79</td>
    <td align="right">68.33</td>
    <td align="right">73.05</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">86.68</td>
    <td align="right">89.02</td>
    <td align="right">89.71</td>
    <td align="right">94.60</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">90.27</td>
    <td align="right">95.96</td>
    <td align="right">95.44</td>
    <td align="right">101.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">84.06</td>
    <td align="right">87.65</td>
    <td align="right">87.42</td>
    <td align="right">91.17</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">104.37</td>
    <td align="right">107.12</td>
    <td align="right">106.81</td>
    <td align="right">112.50</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">141.08</td>
    <td align="right">142.82</td>
    <td align="right">142.24</td>
    <td align="right">148.30</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">78.95</td>
    <td align="right">14.22</td>
    <td align="right">8.33</td>
    <td align="right">17.68</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.46</td>
    <td align="right">29.69</td>
    <td align="right">29.58</td>
    <td align="right">29.85</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.42</td>
    <td align="right">14.48</td>
    <td align="right">14.42</td>
    <td align="right">14.53</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.81</td>
    <td align="right">17.72</td>
    <td align="right">17.78</td>
    <td align="right">17.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.63</td>
    <td align="right">44.21</td>
    <td align="right">31.61</td>
    <td align="right">38.23</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.08</td>
    <td align="right">18.20</td>
    <td align="right">18.14</td>
    <td align="right">18.16</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.21</td>
    <td align="right">21.63</td>
    <td align="right">21.72</td>
    <td align="right">21.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.36</td>
    <td align="right">64.26</td>
    <td align="right">31.87</td>
    <td align="right">51.67</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.59</td>
    <td align="right">21.46</td>
    <td align="right">21.39</td>
    <td align="right">21.46</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.03</td>
    <td align="right">22.98</td>
    <td align="right">23.23</td>
    <td align="right">22.99</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">61.86</td>
    <td align="right">80.02</td>
    <td align="right">33.06</td>
    <td align="right">56.75</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.17</td>
    <td align="right">23.39</td>
    <td align="right">23.38</td>
    <td align="right">23.46</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.05</td>
    <td align="right">25.72</td>
    <td align="right">25.73</td>
    <td align="right">25.74</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">21.44</td>
    <td align="right">30.30</td>
    <td align="right">30.42</td>
    <td align="right">30.28</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">12.45</td>
    <td align="right">14.58</td>
    <td align="right">14.46</td>
    <td align="right">14.46</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">15.86</td>
    <td align="right">17.79</td>
    <td align="right">17.81</td>
    <td align="right">17.78</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">31.77</td>
    <td align="right">47.95</td>
    <td align="right">48.15</td>
    <td align="right">48.10</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">16.16</td>
    <td align="right">18.22</td>
    <td align="right">18.22</td>
    <td align="right">18.26</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">18.21</td>
    <td align="right">21.63</td>
    <td align="right">21.67</td>
    <td align="right">21.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">39.29</td>
    <td align="right">57.74</td>
    <td align="right">58.03</td>
    <td align="right">57.87</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">18.71</td>
    <td align="right">21.46</td>
    <td align="right">21.35</td>
    <td align="right">21.45</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">22.10</td>
    <td align="right">22.98</td>
    <td align="right">23.00</td>
    <td align="right">23.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">59.46</td>
    <td align="right">74.11</td>
    <td align="right">74.15</td>
    <td align="right">75.03</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">22.19</td>
    <td align="right">23.38</td>
    <td align="right">23.47</td>
    <td align="right">23.47</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">24.04</td>
    <td align="right">25.72</td>
    <td align="right">25.70</td>
    <td align="right">25.70</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.03</td>
    <td align="right">20.21</td>
    <td align="right">22.80</td>
    <td align="right">23.72</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.07</td>
    <td align="right">20.27</td>
    <td align="right">22.49</td>
    <td align="right">23.58</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.99</td>
    <td align="right">9.32</td>
    <td align="right">18.59</td>
    <td align="right">16.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.68</td>
    <td align="right">26.25</td>
    <td align="right">24.62</td>
    <td align="right">27.95</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.58</td>
    <td align="right">26.03</td>
    <td align="right">24.29</td>
    <td align="right">27.45</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.91</td>
    <td align="right">13.85</td>
    <td align="right">20.69</td>
    <td align="right">19.90</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.17</td>
    <td align="right">38.01</td>
    <td align="right">26.72</td>
    <td align="right">34.66</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.57</td>
    <td align="right">37.61</td>
    <td align="right">26.25</td>
    <td align="right">34.28</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.84</td>
    <td align="right">16.71</td>
    <td align="right">24.77</td>
    <td align="right">22.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.58</td>
    <td align="right">41.81</td>
    <td align="right">25.88</td>
    <td align="right">36.77</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.44</td>
    <td align="right">44.05</td>
    <td align="right">26.63</td>
    <td align="right">37.76</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.09</td>
    <td align="right">20.17</td>
    <td align="right">21.16</td>
    <td align="right">24.68</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.03</td>
    <td align="right">19.94</td>
    <td align="right">19.93</td>
    <td align="right">19.93</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.14</td>
    <td align="right">20.24</td>
    <td align="right">20.25</td>
    <td align="right">20.25</td>
    <td align="center">5</td>
    <td align="right">2.7379</td>
    <td align="right">7.97</td>
    <td align="right">9.88</td>
    <td align="right">9.88</td>
    <td align="right">9.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.68</td>
    <td align="right">28.12</td>
    <td align="right">28.13</td>
    <td align="right">28.12</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.60</td>
    <td align="right">27.57</td>
    <td align="right">27.58</td>
    <td align="right">27.63</td>
    <td align="center">8</td>
    <td align="right">0.5254</td>
    <td align="right">11.92</td>
    <td align="right">15.03</td>
    <td align="right">15.01</td>
    <td align="right">15.01</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.13</td>
    <td align="right">35.32</td>
    <td align="right">35.30</td>
    <td align="right">35.32</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.52</td>
    <td align="right">34.77</td>
    <td align="right">34.79</td>
    <td align="right">34.78</td>
    <td align="center">11</td>
    <td align="right">0.1223</td>
    <td align="right">13.84</td>
    <td align="right">18.19</td>
    <td align="right">18.20</td>
    <td align="right">18.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.58</td>
    <td align="right">38.70</td>
    <td align="right">38.74</td>
    <td align="right">38.67</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.37</td>
    <td align="right">41.89</td>
    <td align="right">41.92</td>
    <td align="right">41.99</td>
    <td align="center">13</td>
    <td align="right">0.0311</td>
    <td align="right">19.14</td>
    <td align="right">20.73</td>
    <td align="right">20.73</td>
    <td align="right">20.72</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.69</td>
    <td align="right">9.08</td>
    <td align="right">17.46</td>
    <td align="right">15.89</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.02</td>
    <td align="right">20.21</td>
    <td align="right">22.78</td>
    <td align="right">23.69</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">17.07</td>
    <td align="right">20.20</td>
    <td align="right">22.50</td>
    <td align="right">23.56</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.89</td>
    <td align="right">14.43</td>
    <td align="right">20.66</td>
    <td align="right">20.12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.69</td>
    <td align="right">26.21</td>
    <td align="right">24.63</td>
    <td align="right">27.94</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.57</td>
    <td align="right">26.00</td>
    <td align="right">24.32</td>
    <td align="right">27.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.19</td>
    <td align="right">15.41</td>
    <td align="right">20.57</td>
    <td align="right">20.95</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.16</td>
    <td align="right">37.98</td>
    <td align="right">26.73</td>
    <td align="right">34.69</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.64</td>
    <td align="right">37.54</td>
    <td align="right">26.26</td>
    <td align="right">34.32</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.78</td>
    <td align="right">19.88</td>
    <td align="right">20.77</td>
    <td align="right">24.77</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.58</td>
    <td align="right">41.71</td>
    <td align="right">25.89</td>
    <td align="right">36.77</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.41</td>
    <td align="right">44.06</td>
    <td align="right">26.63</td>
    <td align="right">37.77</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4755</td>
    <td align="right">7.52</td>
    <td align="right">9.71</td>
    <td align="right">9.71</td>
    <td align="right">9.71</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">17.03</td>
    <td align="right">19.71</td>
    <td align="right">19.79</td>
    <td align="right">19.93</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">16.99</td>
    <td align="right">20.21</td>
    <td align="right">20.21</td>
    <td align="right">20.19</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4449</td>
    <td align="right">11.71</td>
    <td align="right">14.83</td>
    <td align="right">14.82</td>
    <td align="right">14.81</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">22.69</td>
    <td align="right">28.13</td>
    <td align="right">28.11</td>
    <td align="right">28.11</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">26.58</td>
    <td align="right">27.57</td>
    <td align="right">27.60</td>
    <td align="right">27.61</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0848</td>
    <td align="right">14.29</td>
    <td align="right">17.53</td>
    <td align="right">17.54</td>
    <td align="right">17.53</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">33.12</td>
    <td align="right">35.31</td>
    <td align="right">35.33</td>
    <td align="right">35.24</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">35.59</td>
    <td align="right">34.84</td>
    <td align="right">34.82</td>
    <td align="right">34.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0214</td>
    <td align="right">18.82</td>
    <td align="right">20.71</td>
    <td align="right">20.72</td>
    <td align="right">20.72</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">37.55</td>
    <td align="right">38.70</td>
    <td align="right">38.74</td>
    <td align="right">38.71</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">44.43</td>
    <td align="right">41.91</td>
    <td align="right">41.94</td>
    <td align="right">42.04</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.22</td>
    <td align="right">21.01</td>
    <td align="right">23.99</td>
    <td align="right">24.37</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">47.40</td>
    <td align="right">42.40</td>
    <td align="right">41.48</td>
    <td align="right">40.95</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">27.12</td>
    <td align="right">29.92</td>
    <td align="right">29.23</td>
    <td align="right">30.23</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">26.99</td>
    <td align="right">30.06</td>
    <td align="right">24.12</td>
    <td align="right">30.60</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">52.64</td>
    <td align="right">46.86</td>
    <td align="right">39.29</td>
    <td align="right">43.77</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.79</td>
    <td align="right">39.10</td>
    <td align="right">30.25</td>
    <td align="right">35.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.13</td>
    <td align="right">36.09</td>
    <td align="right">24.59</td>
    <td align="right">34.05</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">60.31</td>
    <td align="right">55.27</td>
    <td align="right">40.06</td>
    <td align="right">48.14</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.58</td>
    <td align="right">45.64</td>
    <td align="right">32.00</td>
    <td align="right">41.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.74</td>
    <td align="right">47.74</td>
    <td align="right">30.30</td>
    <td align="right">42.07</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">63.88</td>
    <td align="right">58.89</td>
    <td align="right">45.97</td>
    <td align="right">52.29</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.43</td>
    <td align="right">58.20</td>
    <td align="right">33.47</td>
    <td align="right">47.38</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">18.22</td>
    <td align="right">20.92</td>
    <td align="right">20.94</td>
    <td align="right">20.93</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">47.43</td>
    <td align="right">38.88</td>
    <td align="right">39.77</td>
    <td align="right">39.82</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">26.88</td>
    <td align="right">27.58</td>
    <td align="right">27.66</td>
    <td align="right">27.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">27.01</td>
    <td align="right">27.89</td>
    <td align="right">27.88</td>
    <td align="right">27.88</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">52.56</td>
    <td align="right">44.74</td>
    <td align="right">44.81</td>
    <td align="right">44.31</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">36.82</td>
    <td align="right">36.50</td>
    <td align="right">36.43</td>
    <td align="right">36.43</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">33.21</td>
    <td align="right">32.93</td>
    <td align="right">32.94</td>
    <td align="right">32.93</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">59.80</td>
    <td align="right">49.01</td>
    <td align="right">49.12</td>
    <td align="right">49.39</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">39.51</td>
    <td align="right">38.59</td>
    <td align="right">38.52</td>
    <td align="right">38.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">39.73</td>
    <td align="right">38.79</td>
    <td align="right">38.79</td>
    <td align="right">38.82</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">63.95</td>
    <td align="right">53.22</td>
    <td align="right">53.32</td>
    <td align="right">53.17</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">52.24</td>
    <td align="right">51.26</td>
    <td align="right">51.16</td>
    <td align="right">50.72</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">124.12</td>
    <td align="right">61.86</td>
    <td align="right">23.23</td>
    <td align="right">55.58</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">28.33</td>
    <td align="right">37.16</td>
    <td align="right">34.52</td>
    <td align="right">36.73</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">16.40</td>
    <td align="right">18.37</td>
    <td align="right">18.60</td>
    <td align="right">18.45</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">19.02</td>
    <td align="right">20.87</td>
    <td align="right">20.94</td>
    <td align="right">20.90</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">73.92</td>
    <td align="right">93.61</td>
    <td align="right">47.36</td>
    <td align="right">74.00</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">27.30</td>
    <td align="right">29.60</td>
    <td align="right">29.60</td>
    <td align="right">29.53</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">27.99</td>
    <td align="right">33.85</td>
    <td align="right">33.83</td>
    <td align="right">33.75</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">146.22</td>
    <td align="right">201.17</td>
    <td align="right">65.42</td>
    <td align="right">136.55</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">40.39</td>
    <td align="right">47.95</td>
    <td align="right">48.05</td>
    <td align="right">48.20</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">52.39</td>
    <td align="right">51.48</td>
    <td align="right">51.38</td>
    <td align="right">51.37</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">251.18</td>
    <td align="right">306.41</td>
    <td align="right">80.06</td>
    <td align="right">196.10</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.19</td>
    <td align="right">64.84</td>
    <td align="right">64.74</td>
    <td align="right">64.74</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.66</td>
    <td align="right">67.40</td>
    <td align="right">67.39</td>
    <td align="right">67.46</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">26.69</td>
    <td align="right">37.99</td>
    <td align="right">37.49</td>
    <td align="right">37.87</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">15.32</td>
    <td align="right">17.51</td>
    <td align="right">17.30</td>
    <td align="right">17.31</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">18.84</td>
    <td align="right">20.80</td>
    <td align="right">20.80</td>
    <td align="right">20.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">74.78</td>
    <td align="right">99.47</td>
    <td align="right">99.24</td>
    <td align="right">99.16</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">24.87</td>
    <td align="right">27.20</td>
    <td align="right">27.26</td>
    <td align="right">27.16</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">28.88</td>
    <td align="right">36.18</td>
    <td align="right">36.23</td>
    <td align="right">36.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">144.66</td>
    <td align="right">195.75</td>
    <td align="right">195.67</td>
    <td align="right">196.11</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">39.74</td>
    <td align="right">49.11</td>
    <td align="right">48.93</td>
    <td align="right">49.09</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">51.97</td>
    <td align="right">50.63</td>
    <td align="right">50.52</td>
    <td align="right">50.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">249.71</td>
    <td align="right">298.82</td>
    <td align="right">299.02</td>
    <td align="right">298.93</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">64.53</td>
    <td align="right">63.55</td>
    <td align="right">63.64</td>
    <td align="right">63.54</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">67.60</td>
    <td align="right">67.40</td>
    <td align="right">67.38</td>
    <td align="right">67.38</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">20.57</td>
    <td align="right">24.44</td>
    <td align="right">25.37</td>
    <td align="right">29.42</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">21.04</td>
    <td align="right">25.33</td>
    <td align="right">25.59</td>
    <td align="right">29.90</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">11.01</td>
    <td align="right">12.33</td>
    <td align="right">20.69</td>
    <td align="right">19.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.97</td>
    <td align="right">39.24</td>
    <td align="right">32.39</td>
    <td align="right">41.26</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">44.63</td>
    <td align="right">40.30</td>
    <td align="right">31.91</td>
    <td align="right">40.72</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">20.79</td>
    <td align="right">22.80</td>
    <td align="right">26.66</td>
    <td align="right">28.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.72</td>
    <td align="right">72.46</td>
    <td align="right">43.11</td>
    <td align="right">65.73</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.35</td>
    <td align="right">72.05</td>
    <td align="right">43.80</td>
    <td align="right">66.02</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">37.93</td>
    <td align="right">40.06</td>
    <td align="right">42.22</td>
    <td align="right">41.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">89.06</td>
    <td align="right">92.26</td>
    <td align="right">47.71</td>
    <td align="right">81.93</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.42</td>
    <td align="right">96.60</td>
    <td align="right">50.98</td>
    <td align="right">85.68</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.27</td>
    <td align="right">52.42</td>
    <td align="right">38.18</td>
    <td align="right">52.21</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.82</td>
    <td align="right">23.91</td>
    <td align="right">23.81</td>
    <td align="right">23.72</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">20.22</td>
    <td align="right">25.08</td>
    <td align="right">25.06</td>
    <td align="right">25.08</td>
    <td align="center">5</td>
    <td align="right">2.7359</td>
    <td align="right">9.70</td>
    <td align="right">11.76</td>
    <td align="right">11.90</td>
    <td align="right">11.71</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">34.37</td>
    <td align="right">41.52</td>
    <td align="right">41.54</td>
    <td align="right">41.48</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">45.57</td>
    <td align="right">46.95</td>
    <td align="right">47.18</td>
    <td align="right">47.18</td>
    <td align="center">8</td>
    <td align="right">0.5434</td>
    <td align="right">21.44</td>
    <td align="right">24.30</td>
    <td align="right">24.31</td>
    <td align="right">24.38</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.67</td>
    <td align="right">69.54</td>
    <td align="right">69.48</td>
    <td align="right">69.45</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.76</td>
    <td align="right">68.25</td>
    <td align="right">68.46</td>
    <td align="right">68.10</td>
    <td align="center">11</td>
    <td align="right">0.1192</td>
    <td align="right">37.92</td>
    <td align="right">41.02</td>
    <td align="right">41.19</td>
    <td align="right">41.06</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.36</td>
    <td align="right">87.15</td>
    <td align="right">87.05</td>
    <td align="right">87.05</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.81</td>
    <td align="right">92.94</td>
    <td align="right">92.91</td>
    <td align="right">93.04</td>
    <td align="center">13</td>
    <td align="right">0.0279</td>
    <td align="right">53.04</td>
    <td align="right">52.55</td>
    <td align="right">52.42</td>
    <td align="right">52.46</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">8.53</td>
    <td align="right">10.11</td>
    <td align="right">18.98</td>
    <td align="right">17.38</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.94</td>
    <td align="right">23.78</td>
    <td align="right">25.01</td>
    <td align="right">28.74</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">18.29</td>
    <td align="right">22.40</td>
    <td align="right">23.91</td>
    <td align="right">27.13</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">23.93</td>
    <td align="right">26.50</td>
    <td align="right">28.08</td>
    <td align="right">30.58</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">34.01</td>
    <td align="right">38.72</td>
    <td align="right">31.76</td>
    <td align="right">40.48</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">44.76</td>
    <td align="right">44.46</td>
    <td align="right">33.83</td>
    <td align="right">44.59</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">38.40</td>
    <td align="right">39.37</td>
    <td align="right">33.64</td>
    <td align="right">40.54</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">65.78</td>
    <td align="right">70.29</td>
    <td align="right">42.36</td>
    <td align="right">64.10</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">71.12</td>
    <td align="right">72.24</td>
    <td align="right">43.93</td>
    <td align="right">66.29</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.14</td>
    <td align="right">53.58</td>
    <td align="right">38.24</td>
    <td align="right">53.98</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">88.03</td>
    <td align="right">92.17</td>
    <td align="right">48.04</td>
    <td align="right">83.44</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.39</td>
    <td align="right">94.11</td>
    <td align="right">49.94</td>
    <td align="right">83.12</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4784</td>
    <td align="right">8.39</td>
    <td align="right">10.85</td>
    <td align="right">10.83</td>
    <td align="right">10.97</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">21.23</td>
    <td align="right">24.89</td>
    <td align="right">25.06</td>
    <td align="right">25.19</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">19.74</td>
    <td align="right">24.68</td>
    <td align="right">24.73</td>
    <td align="right">24.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4458</td>
    <td align="right">21.64</td>
    <td align="right">23.27</td>
    <td align="right">23.35</td>
    <td align="right">23.08</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">36.94</td>
    <td align="right">42.26</td>
    <td align="right">42.09</td>
    <td align="right">42.03</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">44.09</td>
    <td align="right">42.08</td>
    <td align="right">42.21</td>
    <td align="right">42.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">37.95</td>
    <td align="right">40.86</td>
    <td align="right">40.79</td>
    <td align="right">40.73</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">67.59</td>
    <td align="right">69.16</td>
    <td align="right">69.08</td>
    <td align="right">69.09</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">70.66</td>
    <td align="right">69.64</td>
    <td align="right">69.66</td>
    <td align="right">69.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">53.15</td>
    <td align="right">54.14</td>
    <td align="right">54.14</td>
    <td align="right">54.13</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">87.95</td>
    <td align="right">86.39</td>
    <td align="right">86.40</td>
    <td align="right">86.99</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">96.98</td>
    <td align="right">93.07</td>
    <td align="right">93.09</td>
    <td align="right">93.21</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.06</td>
    <td align="right">24.47</td>
    <td align="right">26.10</td>
    <td align="right">29.32</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">49.07</td>
    <td align="right">43.65</td>
    <td align="right">43.23</td>
    <td align="right">42.71</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">34.32</td>
    <td align="right">37.62</td>
    <td align="right">34.03</td>
    <td align="right">37.77</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">39.98</td>
    <td align="right">42.75</td>
    <td align="right">31.00</td>
    <td align="right">43.35</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">63.71</td>
    <td align="right">59.83</td>
    <td align="right">50.86</td>
    <td align="right">56.97</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">61.37</td>
    <td align="right">62.61</td>
    <td align="right">39.24</td>
    <td align="right">54.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.33</td>
    <td align="right">63.88</td>
    <td align="right">40.68</td>
    <td align="right">61.37</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">89.63</td>
    <td align="right">90.72</td>
    <td align="right">63.81</td>
    <td align="right">80.07</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">86.58</td>
    <td align="right">88.75</td>
    <td align="right">43.63</td>
    <td align="right">74.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">82.06</td>
    <td align="right">88.79</td>
    <td align="right">56.69</td>
    <td align="right">82.65</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">110.44</td>
    <td align="right">107.21</td>
    <td align="right">80.61</td>
    <td align="right">100.68</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">131.16</td>
    <td align="right">132.57</td>
    <td align="right">50.07</td>
    <td align="right">103.63</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">21.33</td>
    <td align="right">25.47</td>
    <td align="right">25.30</td>
    <td align="right">25.27</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">49.49</td>
    <td align="right">40.87</td>
    <td align="right">41.01</td>
    <td align="right">41.11</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">33.45</td>
    <td align="right">34.94</td>
    <td align="right">34.08</td>
    <td align="right">34.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">40.45</td>
    <td align="right">41.42</td>
    <td align="right">41.43</td>
    <td align="right">41.45</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">63.77</td>
    <td align="right">58.17</td>
    <td align="right">58.01</td>
    <td align="right">58.46</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">56.07</td>
    <td align="right">55.71</td>
    <td align="right">55.79</td>
    <td align="right">55.91</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">62.41</td>
    <td align="right">60.10</td>
    <td align="right">60.11</td>
    <td align="right">60.05</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">88.91</td>
    <td align="right">80.68</td>
    <td align="right">80.88</td>
    <td align="right">81.10</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">86.35</td>
    <td align="right">80.24</td>
    <td align="right">80.06</td>
    <td align="right">80.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">81.62</td>
    <td align="right">80.72</td>
    <td align="right">86.45</td>
    <td align="right">86.24</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">109.63</td>
    <td align="right">98.36</td>
    <td align="right">98.52</td>
    <td align="right">98.63</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">133.33</td>
    <td align="right">120.33</td>
    <td align="right">120.36</td>
    <td align="right">120.01</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">32.27</td>
    <td align="right">7.10</td>
    <td align="right">5.42</td>
    <td align="right">12.30</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">65.05</td>
    <td align="right">59.87</td>
    <td align="right">40.86</td>
    <td align="right">49.69</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">21.00</td>
    <td align="right">21.22</td>
    <td align="right">24.07</td>
    <td align="right">26.76</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">24.93</td>
    <td align="right">25.53</td>
    <td align="right">26.37</td>
    <td align="right">27.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">100.87</td>
    <td align="right">87.67</td>
    <td align="right">41.61</td>
    <td align="right">63.56</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.27</td>
    <td align="right">23.41</td>
    <td align="right">24.36</td>
    <td align="right">27.48</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.74</td>
    <td align="right">28.49</td>
    <td align="right">29.06</td>
    <td align="right">31.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">126.69</td>
    <td align="right">105.50</td>
    <td align="right">40.47</td>
    <td align="right">72.20</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.25</td>
    <td align="right">25.85</td>
    <td align="right">26.80</td>
    <td align="right">30.25</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.55</td>
    <td align="right">30.54</td>
    <td align="right">30.15</td>
    <td align="right">32.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">163.21</td>
    <td align="right">134.69</td>
    <td align="right">41.07</td>
    <td align="right">87.63</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">27.44</td>
    <td align="right">27.08</td>
    <td align="right">28.17</td>
    <td align="right">31.14</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">32.60</td>
    <td align="right">31.89</td>
    <td align="right">32.92</td>
    <td align="right">35.37</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1535</td>
    <td align="right">65.21</td>
    <td align="right">62.27</td>
    <td align="right">62.31</td>
    <td align="right">68.21</td>
    <td align="center">4</td>
    <td align="right">3.3223</td>
    <td align="right">20.87</td>
    <td align="right">21.06</td>
    <td align="right">23.77</td>
    <td align="right">25.70</td>
    <td align="center">5</td>
    <td align="right">3.0704</td>
    <td align="right">24.90</td>
    <td align="right">25.39</td>
    <td align="right">27.22</td>
    <td align="right">28.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3124</td>
    <td align="right">104.29</td>
    <td align="right">91.04</td>
    <td align="right">90.56</td>
    <td align="right">96.94</td>
    <td align="center">5</td>
    <td align="right">1.0493</td>
    <td align="right">22.50</td>
    <td align="right">23.76</td>
    <td align="right">24.93</td>
    <td align="right">27.78</td>
    <td align="center">6</td>
    <td align="right">0.8146</td>
    <td align="right">27.58</td>
    <td align="right">28.07</td>
    <td align="right">28.85</td>
    <td align="right">31.67</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0479</td>
    <td align="right">125.58</td>
    <td align="right">110.42</td>
    <td align="right">109.66</td>
    <td align="right">116.57</td>
    <td align="center">6</td>
    <td align="right">0.4013</td>
    <td align="right">25.41</td>
    <td align="right">25.92</td>
    <td align="right">26.85</td>
    <td align="right">30.23</td>
    <td align="center">7</td>
    <td align="right">0.2937</td>
    <td align="right">29.13</td>
    <td align="right">31.24</td>
    <td align="right">30.23</td>
    <td align="right">33.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0061</td>
    <td align="right">167.37</td>
    <td align="right">141.36</td>
    <td align="right">141.30</td>
    <td align="right">145.80</td>
    <td align="center">7</td>
    <td align="right">0.1916</td>
    <td align="right">27.26</td>
    <td align="right">27.09</td>
    <td align="right">28.08</td>
    <td align="right">31.28</td>
    <td align="center">8</td>
    <td align="right">0.1274</td>
    <td align="right">31.60</td>
    <td align="right">32.81</td>
    <td align="right">33.08</td>
    <td align="right">35.54</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.38</td>
    <td align="right">43.20</td>
    <td align="right">33.91</td>
    <td align="right">38.96</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.57</td>
    <td align="right">43.71</td>
    <td align="right">35.33</td>
    <td align="right">40.55</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.70</td>
    <td align="right">29.28</td>
    <td align="right">29.08</td>
    <td align="right">33.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.65</td>
    <td align="right">59.87</td>
    <td align="right">34.34</td>
    <td align="right">47.07</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.16</td>
    <td align="right">59.92</td>
    <td align="right">36.25</td>
    <td align="right">48.44</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.89</td>
    <td align="right">37.75</td>
    <td align="right">27.72</td>
    <td align="right">37.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">37.82</td>
    <td align="right">77.94</td>
    <td align="right">35.31</td>
    <td align="right">58.35</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">42.15</td>
    <td align="right">78.59</td>
    <td align="right">37.16</td>
    <td align="right">58.14</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.23</td>
    <td align="right">54.23</td>
    <td align="right">37.29</td>
    <td align="right">50.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.46</td>
    <td align="right">90.97</td>
    <td align="right">34.37</td>
    <td align="right">62.34</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.62</td>
    <td align="right">96.73</td>
    <td align="right">38.79</td>
    <td align="right">68.15</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">28.90</td>
    <td align="right">54.54</td>
    <td align="right">37.67</td>
    <td align="right">50.72</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4720</td>
    <td align="right">24.43</td>
    <td align="right">42.28</td>
    <td align="right">42.88</td>
    <td align="right">44.82</td>
    <td align="center">5</td>
    <td align="right">2.3433</td>
    <td align="right">26.56</td>
    <td align="right">42.58</td>
    <td align="right">42.70</td>
    <td align="right">44.94</td>
    <td align="center">5</td>
    <td align="right">2.7237</td>
    <td align="right">17.60</td>
    <td align="right">29.86</td>
    <td align="right">30.06</td>
    <td align="right">33.47</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4178</td>
    <td align="right">29.48</td>
    <td align="right">56.81</td>
    <td align="right">56.39</td>
    <td align="right">58.95</td>
    <td align="center">8</td>
    <td align="right">0.3776</td>
    <td align="right">32.41</td>
    <td align="right">56.97</td>
    <td align="right">56.88</td>
    <td align="right">59.76</td>
    <td align="center">8</td>
    <td align="right">0.5409</td>
    <td align="right">16.92</td>
    <td align="right">37.22</td>
    <td align="right">37.00</td>
    <td align="right">37.65</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0827</td>
    <td align="right">37.97</td>
    <td align="right">75.96</td>
    <td align="right">76.05</td>
    <td align="right">78.62</td>
    <td align="center">11</td>
    <td align="right">0.0632</td>
    <td align="right">42.00</td>
    <td align="right">77.84</td>
    <td align="right">76.97</td>
    <td align="right">78.83</td>
    <td align="center">11</td>
    <td align="right">0.1175</td>
    <td align="right">27.22</td>
    <td align="right">49.34</td>
    <td align="right">48.97</td>
    <td align="right">53.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0174</td>
    <td align="right">41.09</td>
    <td align="right">84.34</td>
    <td align="right">84.17</td>
    <td align="right">87.16</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">47.16</td>
    <td align="right">89.93</td>
    <td align="right">90.74</td>
    <td align="right">92.06</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">27.64</td>
    <td align="right">49.36</td>
    <td align="right">49.03</td>
    <td align="right">52.57</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">18.01</td>
    <td align="right">29.06</td>
    <td align="right">28.68</td>
    <td align="right">32.49</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.80</td>
    <td align="right">31.07</td>
    <td align="right">30.94</td>
    <td align="right">34.85</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.39</td>
    <td align="right">30.85</td>
    <td align="right">30.73</td>
    <td align="right">34.66</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">18.05</td>
    <td align="right">44.72</td>
    <td align="right">34.67</td>
    <td align="right">44.67</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.90</td>
    <td align="right">39.24</td>
    <td align="right">29.55</td>
    <td align="right">38.94</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.75</td>
    <td align="right">46.91</td>
    <td align="right">37.42</td>
    <td align="right">46.84</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.09</td>
    <td align="right">53.70</td>
    <td align="right">36.64</td>
    <td align="right">49.69</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.89</td>
    <td align="right">57.53</td>
    <td align="right">39.97</td>
    <td align="right">53.35</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.76</td>
    <td align="right">57.56</td>
    <td align="right">39.59</td>
    <td align="right">53.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">28.41</td>
    <td align="right">54.17</td>
    <td align="right">37.30</td>
    <td align="right">50.13</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">33.00</td>
    <td align="right">59.68</td>
    <td align="right">40.73</td>
    <td align="right">54.91</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">34.53</td>
    <td align="right">59.36</td>
    <td align="right">40.33</td>
    <td align="right">54.52</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4745</td>
    <td align="right">17.99</td>
    <td align="right">29.81</td>
    <td align="right">30.11</td>
    <td align="right">33.22</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">19.89</td>
    <td align="right">30.02</td>
    <td align="right">29.74</td>
    <td align="right">33.85</td>
    <td align="center">5</td>
    <td align="right">2.3490</td>
    <td align="right">20.43</td>
    <td align="right">29.97</td>
    <td align="right">29.83</td>
    <td align="right">34.27</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4442</td>
    <td align="right">18.10</td>
    <td align="right">38.35</td>
    <td align="right">37.91</td>
    <td align="right">38.87</td>
    <td align="center">8</td>
    <td align="right">0.4151</td>
    <td align="right">18.89</td>
    <td align="right">38.38</td>
    <td align="right">37.89</td>
    <td align="right">38.36</td>
    <td align="center">8</td>
    <td align="right">0.3796</td>
    <td align="right">20.82</td>
    <td align="right">38.39</td>
    <td align="right">38.74</td>
    <td align="right">39.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0865</td>
    <td align="right">28.09</td>
    <td align="right">48.75</td>
    <td align="right">48.71</td>
    <td align="right">52.11</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">31.86</td>
    <td align="right">51.51</td>
    <td align="right">51.55</td>
    <td align="right">55.21</td>
    <td align="center">11</td>
    <td align="right">0.0642</td>
    <td align="right">32.71</td>
    <td align="right">51.65</td>
    <td align="right">51.22</td>
    <td align="right">55.35</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0179</td>
    <td align="right">29.12</td>
    <td align="right">49.02</td>
    <td align="right">48.76</td>
    <td align="right">52.28</td>
    <td align="center">13</td>
    <td align="right">0.0166</td>
    <td align="right">33.49</td>
    <td align="right">53.54</td>
    <td align="right">53.32</td>
    <td align="right">57.21</td>
    <td align="center">14</td>
    <td align="right">0.0107</td>
    <td align="right">34.96</td>
    <td align="right">53.00</td>
    <td align="right">52.81</td>
    <td align="right">57.04</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">27.02</td>
    <td align="right">43.28</td>
    <td align="right">32.75</td>
    <td align="right">38.13</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.85</td>
    <td align="right">55.54</td>
    <td align="right">37.50</td>
    <td align="right">46.31</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">36.38</td>
    <td align="right">65.39</td>
    <td align="right">40.22</td>
    <td align="right">52.75</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">35.69</td>
    <td align="right">61.22</td>
    <td align="right">33.63</td>
    <td align="right">48.40</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">39.94</td>
    <td align="right">61.83</td>
    <td align="right">36.42</td>
    <td align="right">50.55</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">44.55</td>
    <td align="right">82.25</td>
    <td align="right">38.95</td>
    <td align="right">60.71</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">40.95</td>
    <td align="right">74.37</td>
    <td align="right">33.47</td>
    <td align="right">55.33</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">46.93</td>
    <td align="right">79.36</td>
    <td align="right">36.51</td>
    <td align="right">60.07</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">48.53</td>
    <td align="right">91.11</td>
    <td align="right">38.14</td>
    <td align="right">64.12</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">51.67</td>
    <td align="right">99.18</td>
    <td align="right">34.43</td>
    <td align="right">68.25</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">56.02</td>
    <td align="right">101.10</td>
    <td align="right">36.42</td>
    <td align="right">68.72</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">64.19</td>
    <td align="right">120.53</td>
    <td align="right">40.29</td>
    <td align="right">81.11</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3091</td>
    <td align="right">27.14</td>
    <td align="right">42.71</td>
    <td align="right">42.66</td>
    <td align="right">45.23</td>
    <td align="center">6</td>
    <td align="right">2.2991</td>
    <td align="right">32.84</td>
    <td align="right">49.13</td>
    <td align="right">48.83</td>
    <td align="right">51.10</td>
    <td align="center">7</td>
    <td align="right">2.3472</td>
    <td align="right">36.30</td>
    <td align="right">61.00</td>
    <td align="right">61.14</td>
    <td align="right">65.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4211</td>
    <td align="right">35.83</td>
    <td align="right">57.25</td>
    <td align="right">56.73</td>
    <td align="right">59.91</td>
    <td align="center">7</td>
    <td align="right">0.3930</td>
    <td align="right">39.99</td>
    <td align="right">62.19</td>
    <td align="right">60.52</td>
    <td align="right">63.05</td>
    <td align="center">10</td>
    <td align="right">0.3516</td>
    <td align="right">45.64</td>
    <td align="right">80.83</td>
    <td align="right">80.20</td>
    <td align="right">82.72</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0870</td>
    <td align="right">40.68</td>
    <td align="right">67.87</td>
    <td align="right">67.12</td>
    <td align="right">71.52</td>
    <td align="center">10</td>
    <td align="right">0.0719</td>
    <td align="right">47.17</td>
    <td align="right">79.59</td>
    <td align="right">79.16</td>
    <td align="right">82.11</td>
    <td align="center">11</td>
    <td align="right">0.0500</td>
    <td align="right">48.49</td>
    <td align="right">85.55</td>
    <td align="right">85.35</td>
    <td align="right">88.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0183</td>
    <td align="right">51.69</td>
    <td align="right">92.78</td>
    <td align="right">90.79</td>
    <td align="right">94.37</td>
    <td align="center">12</td>
    <td align="right">0.0143</td>
    <td align="right">55.72</td>
    <td align="right">91.97</td>
    <td align="right">90.56</td>
    <td align="right">95.67</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">63.22</td>
    <td align="right">118.78</td>
    <td align="right">120.53</td>
    <td align="right">121.62</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="4"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
    <th>mixed<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">63.48</td>
    <td align="right">33.93</td>
    <td align="right">16.77</td>
    <td align="right">37.50</td>
  </tr>
</table>
<table>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">76.54</td>
    <td align="right">74.48</td>
    <td align="right">46.64</td>
    <td align="right">59.51</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.10</td>
    <td align="right">21.17</td>
    <td align="right">24.47</td>
    <td align="right">27.73</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">26.67</td>
    <td align="right">27.55</td>
    <td align="right">28.79</td>
    <td align="right">29.65</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">127.86</td>
    <td align="right">110.86</td>
    <td align="right">48.54</td>
    <td align="right">78.69</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">25.41</td>
    <td align="right">25.50</td>
    <td align="right">26.63</td>
    <td align="right">30.08</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">32.83</td>
    <td align="right">33.65</td>
    <td align="right">34.41</td>
    <td align="right">36.14</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">254.52</td>
    <td align="right">215.04</td>
    <td align="right">63.63</td>
    <td align="right">138.56</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.50</td>
    <td align="right">38.17</td>
    <td align="right">39.18</td>
    <td align="right">43.54</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">48.48</td>
    <td align="right">48.76</td>
    <td align="right">48.08</td>
    <td align="right">51.07</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">436.72</td>
    <td align="right">356.21</td>
    <td align="right">78.52</td>
    <td align="right">217.47</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">45.11</td>
    <td align="right">44.91</td>
    <td align="right">46.46</td>
    <td align="right">50.62</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">60.99</td>
    <td align="right">62.47</td>
    <td align="right">63.60</td>
    <td align="right">65.71</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,K></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1483</td>
    <td align="right">72.65</td>
    <td align="right">71.62</td>
    <td align="right">72.09</td>
    <td align="right">79.34</td>
    <td align="center">4</td>
    <td align="right">3.3516</td>
    <td align="right">21.10</td>
    <td align="right">21.86</td>
    <td align="right">25.31</td>
    <td align="right">27.27</td>
    <td align="center">5</td>
    <td align="right">3.0386</td>
    <td align="right">26.90</td>
    <td align="right">27.18</td>
    <td align="right">28.56</td>
    <td align="right">29.30</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3160</td>
    <td align="right">138.99</td>
    <td align="right">119.82</td>
    <td align="right">119.78</td>
    <td align="right">127.43</td>
    <td align="center">5</td>
    <td align="right">1.0284</td>
    <td align="right">27.64</td>
    <td align="right">27.36</td>
    <td align="right">28.82</td>
    <td align="right">32.00</td>
    <td align="center">6</td>
    <td align="right">0.8263</td>
    <td align="right">51.82</td>
    <td align="right">52.00</td>
    <td align="right">52.07</td>
    <td align="right">54.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0450</td>
    <td align="right">351.35</td>
    <td align="right">290.50</td>
    <td align="right">288.03</td>
    <td align="right">296.08</td>
    <td align="center">6</td>
    <td align="right">0.4002</td>
    <td align="right">37.51</td>
    <td align="right">37.93</td>
    <td align="right">39.07</td>
    <td align="right">43.07</td>
    <td align="center">7</td>
    <td align="right">0.2896</td>
    <td align="right">47.86</td>
    <td align="right">48.82</td>
    <td align="right">48.06</td>
    <td align="right">51.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0071</td>
    <td align="right">438.19</td>
    <td align="right">361.46</td>
    <td align="right">360.28</td>
    <td align="right">368.32</td>
    <td align="center">7</td>
    <td align="right">0.1867</td>
    <td align="right">45.19</td>
    <td align="right">44.93</td>
    <td align="right">45.90</td>
    <td align="right">50.68</td>
    <td align="center">8</td>
    <td align="right">0.1186</td>
    <td align="right">61.67</td>
    <td align="right">62.95</td>
    <td align="right">63.96</td>
    <td align="right">65.93</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">25.96</td>
    <td align="right">44.45</td>
    <td align="right">35.46</td>
    <td align="right">40.98</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">28.48</td>
    <td align="right">44.10</td>
    <td align="right">36.92</td>
    <td align="right">41.18</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">21.69</td>
    <td align="right">54.68</td>
    <td align="right">54.95</td>
    <td align="right">59.28</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">35.02</td>
    <td align="right">63.52</td>
    <td align="right">39.60</td>
    <td align="right">52.04</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">38.83</td>
    <td align="right">63.04</td>
    <td align="right">41.27</td>
    <td align="right">53.08</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">19.93</td>
    <td align="right">43.34</td>
    <td align="right">33.37</td>
    <td align="right">43.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">56.93</td>
    <td align="right">91.14</td>
    <td align="right">49.58</td>
    <td align="right">72.11</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">64.10</td>
    <td align="right">95.69</td>
    <td align="right">57.53</td>
    <td align="right">76.57</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">47.28</td>
    <td align="right">77.10</td>
    <td align="right">59.86</td>
    <td align="right">73.90</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">74.55</td>
    <td align="right">114.23</td>
    <td align="right">61.94</td>
    <td align="right">88.20</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">84.79</td>
    <td align="right">127.54</td>
    <td align="right">74.18</td>
    <td align="right">101.28</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">59.09</td>
    <td align="right">91.18</td>
    <td align="right">73.70</td>
    <td align="right">87.51</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4543</td>
    <td align="right">25.95</td>
    <td align="right">42.33</td>
    <td align="right">42.95</td>
    <td align="right">44.95</td>
    <td align="center">5</td>
    <td align="right">2.3258</td>
    <td align="right">30.07</td>
    <td align="right">42.66</td>
    <td align="right">42.74</td>
    <td align="right">44.96</td>
    <td align="center">5</td>
    <td align="right">2.7344</td>
    <td align="right">18.16</td>
    <td align="right">31.81</td>
    <td align="right">32.47</td>
    <td align="right">35.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4223</td>
    <td align="right">33.49</td>
    <td align="right">59.47</td>
    <td align="right">59.16</td>
    <td align="right">61.59</td>
    <td align="center">8</td>
    <td align="right">0.3748</td>
    <td align="right">37.14</td>
    <td align="right">59.04</td>
    <td align="right">59.13</td>
    <td align="right">61.54</td>
    <td align="center">8</td>
    <td align="right">0.5420</td>
    <td align="right">19.68</td>
    <td align="right">40.91</td>
    <td align="right">41.13</td>
    <td align="right">41.62</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0775</td>
    <td align="right">57.77</td>
    <td align="right">89.72</td>
    <td align="right">89.73</td>
    <td align="right">92.41</td>
    <td align="center">11</td>
    <td align="right">0.0650</td>
    <td align="right">73.75</td>
    <td align="right">102.07</td>
    <td align="right">101.08</td>
    <td align="right">103.29</td>
    <td align="center">11</td>
    <td align="right">0.1178</td>
    <td align="right">54.40</td>
    <td align="right">80.88</td>
    <td align="right">80.18</td>
    <td align="right">84.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0157</td>
    <td align="right">75.20</td>
    <td align="right">107.74</td>
    <td align="right">107.52</td>
    <td align="right">110.66</td>
    <td align="center">14</td>
    <td align="right">0.0115</td>
    <td align="right">84.86</td>
    <td align="right">119.43</td>
    <td align="right">120.09</td>
    <td align="right">121.48</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">59.06</td>
    <td align="right">87.68</td>
    <td align="right">87.07</td>
    <td align="right">90.98</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.23</td>
    <td align="right">30.73</td>
    <td align="right">30.70</td>
    <td align="right">34.93</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">20.11</td>
    <td align="right">32.38</td>
    <td align="right">32.44</td>
    <td align="right">36.71</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">20.50</td>
    <td align="right">32.05</td>
    <td align="right">32.04</td>
    <td align="right">36.24</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">37.34</td>
    <td align="right">71.92</td>
    <td align="right">62.33</td>
    <td align="right">72.30</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">20.64</td>
    <td align="right">44.55</td>
    <td align="right">34.82</td>
    <td align="right">44.22</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">24.75</td>
    <td align="right">50.63</td>
    <td align="right">42.11</td>
    <td align="right">51.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">50.82</td>
    <td align="right">78.72</td>
    <td align="right">62.27</td>
    <td align="right">76.13</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">51.69</td>
    <td align="right">80.63</td>
    <td align="right">62.52</td>
    <td align="right">76.37</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">53.48</td>
    <td align="right">81.22</td>
    <td align="right">63.47</td>
    <td align="right">77.22</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">61.27</td>
    <td align="right">92.00</td>
    <td align="right">75.03</td>
    <td align="right">89.04</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">63.55</td>
    <td align="right">97.04</td>
    <td align="right">78.18</td>
    <td align="right">92.32</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">65.09</td>
    <td align="right">98.30</td>
    <td align="right">78.53</td>
    <td align="right">93.60</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4716</td>
    <td align="right">18.17</td>
    <td align="right">31.51</td>
    <td align="right">31.89</td>
    <td align="right">35.31</td>
    <td align="center">5</td>
    <td align="right">2.4474</td>
    <td align="right">20.01</td>
    <td align="right">31.50</td>
    <td align="right">31.45</td>
    <td align="right">35.56</td>
    <td align="center">5</td>
    <td align="right">2.3181</td>
    <td align="right">29.56</td>
    <td align="right">40.55</td>
    <td align="right">40.41</td>
    <td align="right">44.93</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4430</td>
    <td align="right">36.07</td>
    <td align="right">62.99</td>
    <td align="right">62.67</td>
    <td align="right">63.69</td>
    <td align="center">8</td>
    <td align="right">0.4208</td>
    <td align="right">22.46</td>
    <td align="right">43.20</td>
    <td align="right">42.99</td>
    <td align="right">43.62</td>
    <td align="center">8</td>
    <td align="right">0.3766</td>
    <td align="right">24.63</td>
    <td align="right">42.37</td>
    <td align="right">43.10</td>
    <td align="right">43.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">50.69</td>
    <td align="right">74.74</td>
    <td align="right">74.13</td>
    <td align="right">76.88</td>
    <td align="center">11</td>
    <td align="right">0.0774</td>
    <td align="right">53.16</td>
    <td align="right">75.13</td>
    <td align="right">75.00</td>
    <td align="right">79.28</td>
    <td align="center">11</td>
    <td align="right">0.0647</td>
    <td align="right">53.62</td>
    <td align="right">75.48</td>
    <td align="right">75.00</td>
    <td align="right">79.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0176</td>
    <td align="right">60.95</td>
    <td align="right">88.59</td>
    <td align="right">88.10</td>
    <td align="right">90.36</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">63.68</td>
    <td align="right">91.03</td>
    <td align="right">90.71</td>
    <td align="right">94.97</td>
    <td align="center">14</td>
    <td align="right">0.0118</td>
    <td align="right">65.26</td>
    <td align="right">91.06</td>
    <td align="right">91.18</td>
    <td align="right">95.76</td>
  </tr>
  <tr><th colspan="19">branchful</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">28.81</td>
    <td align="right">44.83</td>
    <td align="right">35.72</td>
    <td align="right">40.69</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">35.57</td>
    <td align="right">59.29</td>
    <td align="right">43.49</td>
    <td align="right">51.10</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">38.36</td>
    <td align="right">65.69</td>
    <td align="right">41.97</td>
    <td align="right">53.76</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">39.54</td>
    <td align="right">64.00</td>
    <td align="right">37.40</td>
    <td align="right">52.31</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">47.03</td>
    <td align="right">66.69</td>
    <td align="right">41.91</td>
    <td align="right">55.58</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">48.05</td>
    <td align="right">85.50</td>
    <td align="right">41.72</td>
    <td align="right">63.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">58.62</td>
    <td align="right">87.79</td>
    <td align="right">50.90</td>
    <td align="right">70.98</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">72.08</td>
    <td align="right">100.27</td>
    <td align="right">59.83</td>
    <td align="right">81.86</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">83.61</td>
    <td align="right">116.70</td>
    <td align="right">62.76</td>
    <td align="right">89.58</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">79.50</td>
    <td align="right">120.88</td>
    <td align="right">62.52</td>
    <td align="right">93.93</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">94.07</td>
    <td align="right">133.61</td>
    <td align="right">73.36</td>
    <td align="right">104.39</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">108.16</td>
    <td align="right">149.37</td>
    <td align="right">63.33</td>
    <td align="right">107.61</td>
  </tr>
  <tr><th colspan="19">branchless</th></tr>
  <tr>
    <th></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="6"><code>filter&lt;int,1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="6"><code>filter&lt;int,1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>mixed<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3259</td>
    <td align="right">28.83</td>
    <td align="right">42.83</td>
    <td align="right">42.74</td>
    <td align="right">45.32</td>
    <td align="center">6</td>
    <td align="right">2.2935</td>
    <td align="right">36.50</td>
    <td align="right">52.50</td>
    <td align="right">52.38</td>
    <td align="right">54.95</td>
    <td align="center">7</td>
    <td align="right">2.3470</td>
    <td align="right">39.29</td>
    <td align="right">61.29</td>
    <td align="right">61.66</td>
    <td align="right">65.92</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4145</td>
    <td align="right">41.64</td>
    <td align="right">59.79</td>
    <td align="right">59.03</td>
    <td align="right">62.52</td>
    <td align="center">7</td>
    <td align="right">0.3870</td>
    <td align="right">47.19</td>
    <td align="right">71.16</td>
    <td align="right">69.66</td>
    <td align="right">72.18</td>
    <td align="center">10</td>
    <td align="right">0.3500</td>
    <td align="right">51.08</td>
    <td align="right">83.16</td>
    <td align="right">82.88</td>
    <td align="right">85.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0844</td>
    <td align="right">58.28</td>
    <td align="right">76.52</td>
    <td align="right">75.91</td>
    <td align="right">80.10</td>
    <td align="center">10</td>
    <td align="right">0.0712</td>
    <td align="right">72.53</td>
    <td align="right">105.14</td>
    <td align="right">105.52</td>
    <td align="right">108.52</td>
    <td align="center">11</td>
    <td align="right">0.0490</td>
    <td align="right">76.56</td>
    <td align="right">104.11</td>
    <td align="right">104.20</td>
    <td align="right">107.43</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0203</td>
    <td align="right">79.22</td>
    <td align="right">111.01</td>
    <td align="right">108.91</td>
    <td align="right">112.57</td>
    <td align="center">12</td>
    <td align="right">0.0150</td>
    <td align="right">93.59</td>
    <td align="right">127.12</td>
    <td align="right">125.87</td>
    <td align="right">131.04</td>
    <td align="center">15</td>
    <td align="right">0.0074</td>
    <td align="right">107.83</td>
    <td align="right">146.19</td>
    <td align="right">147.09</td>
    <td align="right">149.55</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
