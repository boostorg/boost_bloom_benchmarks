# Experimental results for [candidate Boost Bloom Library](https://github.com/joaquintides/bloom)

The tables show the false positive rate (FPR) and execution times in nanoseconds per operation 
for nine different configurations of `boost::bloom::filter<int, ...>`
where `N` elements have been inserted. Filters are constructed with a capacity
`c*N` (bits), so `c` is the number of bits used per element. For each combination of `c` and
a given filter configuration, we have selected the optimum value of `K` (that yielding the minimum FPR).
Standard release-mode settings are used; 
AVX2 is indicated for Visual Studio builds (`/arch:AVX2`) and 64-bit GCC/Clang builds (`-mavx2`),
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
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">25.65</td>
    <td align="right">4.41</td>
    <td align="right">3.47</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">11.13</td>
    <td align="right">10.69</td>
    <td align="right">16.64</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">3.99</td>
    <td align="right">4.34</td>
    <td align="right">4.34</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">4.81</td>
    <td align="right">5.03</td>
    <td align="right">5.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">16.69</td>
    <td align="right">15.48</td>
    <td align="right">17.59</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">4.77</td>
    <td align="right">4.90</td>
    <td align="right">4.93</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">5.38</td>
    <td align="right">5.47</td>
    <td align="right">5.47</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">20.77</td>
    <td align="right">18.11</td>
    <td align="right">16.37</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">5.38</td>
    <td align="right">5.28</td>
    <td align="right">5.27</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">6.21</td>
    <td align="right">6.25</td>
    <td align="right">6.25</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">26.49</td>
    <td align="right">22.97</td>
    <td align="right">16.67</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">6.14</td>
    <td align="right">5.86</td>
    <td align="right">5.87</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">6.66</td>
    <td align="right">6.53</td>
    <td align="right">6.55</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">5.04</td>
    <td align="right">5.70</td>
    <td align="right">5.70</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">5.23</td>
    <td align="right">6.55</td>
    <td align="right">6.48</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.91</td>
    <td align="right">3.25</td>
    <td align="right">3.26</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">6.46</td>
    <td align="right">8.81</td>
    <td align="right">8.82</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">8.33</td>
    <td align="right">9.83</td>
    <td align="right">9.83</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.47</td>
    <td align="right">3.11</td>
    <td align="right">3.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">9.21</td>
    <td align="right">13.18</td>
    <td align="right">13.19</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">16.85</td>
    <td align="right">14.99</td>
    <td align="right">14.99</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.71</td>
    <td align="right">5.72</td>
    <td align="right">3.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">11.00</td>
    <td align="right">14.87</td>
    <td align="right">14.88</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">12.14</td>
    <td align="right">16.09</td>
    <td align="right">16.13</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.74</td>
    <td align="right">5.76</td>
    <td align="right">3.84</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.90</td>
    <td align="right">3.19</td>
    <td align="right">3.21</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.37</td>
    <td align="right">5.03</td>
    <td align="right">4.99</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.53</td>
    <td align="right">4.93</td>
    <td align="right">5.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.02</td>
    <td align="right">3.31</td>
    <td align="right">3.28</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">3.17</td>
    <td align="right">4.41</td>
    <td align="right">4.42</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">4.45</td>
    <td align="right">5.06</td>
    <td align="right">5.07</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.39</td>
    <td align="right">5.42</td>
    <td align="right">3.72</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">6.95</td>
    <td align="right">7.64</td>
    <td align="right">5.87</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">7.79</td>
    <td align="right">7.49</td>
    <td align="right">5.78</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.43</td>
    <td align="right">5.47</td>
    <td align="right">3.75</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">7.94</td>
    <td align="right">8.96</td>
    <td align="right">5.85</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">8.22</td>
    <td align="right">8.95</td>
    <td align="right">5.84</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.82</td>
    <td align="right">6.92</td>
    <td align="right">13.52</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">11.41</td>
    <td align="right">8.87</td>
    <td align="right">17.31</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.39</td>
    <td align="right">10.73</td>
    <td align="right">10.82</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.26</td>
    <td align="right">8.12</td>
    <td align="right">12.39</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.31</td>
    <td align="right">9.41</td>
    <td align="right">14.23</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">14.06</td>
    <td align="right">15.34</td>
    <td align="right">15.39</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">10.87</td>
    <td align="right">10.27</td>
    <td align="right">11.97</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">15.23</td>
    <td align="right">12.49</td>
    <td align="right">15.18</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">16.36</td>
    <td align="right">16.44</td>
    <td align="right">16.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.31</td>
    <td align="right">12.67</td>
    <td align="right">13.12</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.58</td>
    <td align="right">14.02</td>
    <td align="right">14.84</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">21.52</td>
    <td align="right">22.04</td>
    <td align="right">22.16</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">29.86</td>
    <td align="right">17.20</td>
    <td align="right">6.33</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.23</td>
    <td align="right">13.05</td>
    <td align="right">17.89</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">4.80</td>
    <td align="right">5.12</td>
    <td align="right">5.12</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">5.84</td>
    <td align="right">6.02</td>
    <td align="right">6.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">19.59</td>
    <td align="right">18.27</td>
    <td align="right">18.30</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">5.38</td>
    <td align="right">5.59</td>
    <td align="right">5.53</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">6.13</td>
    <td align="right">6.15</td>
    <td align="right">6.18</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">25.12</td>
    <td align="right">23.62</td>
    <td align="right">17.44</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">6.31</td>
    <td align="right">6.09</td>
    <td align="right">6.11</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">7.25</td>
    <td align="right">7.22</td>
    <td align="right">7.21</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">35.08</td>
    <td align="right">31.74</td>
    <td align="right">17.95</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">8.14</td>
    <td align="right">7.92</td>
    <td align="right">7.93</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">8.73</td>
    <td align="right">8.57</td>
    <td align="right">8.28</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">6.08</td>
    <td align="right">6.86</td>
    <td align="right">6.88</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">6.26</td>
    <td align="right">7.91</td>
    <td align="right">7.84</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.57</td>
    <td align="right">3.39</td>
    <td align="right">3.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">7.32</td>
    <td align="right">9.67</td>
    <td align="right">9.69</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">9.14</td>
    <td align="right">10.89</td>
    <td align="right">10.92</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.93</td>
    <td align="right">3.65</td>
    <td align="right">3.64</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">10.84</td>
    <td align="right">14.51</td>
    <td align="right">14.45</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">17.53</td>
    <td align="right">16.86</td>
    <td align="right">16.88</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">6.87</td>
    <td align="right">7.03</td>
    <td align="right">4.86</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">13.63</td>
    <td align="right">16.78</td>
    <td align="right">16.87</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">15.11</td>
    <td align="right">19.04</td>
    <td align="right">18.97</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">7.83</td>
    <td align="right">8.08</td>
    <td align="right">5.62</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.58</td>
    <td align="right">4.05</td>
    <td align="right">4.04</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.19</td>
    <td align="right">6.10</td>
    <td align="right">6.01</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.31</td>
    <td align="right">5.94</td>
    <td align="right">6.04</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.45</td>
    <td align="right">3.94</td>
    <td align="right">3.90</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.66</td>
    <td align="right">5.05</td>
    <td align="right">5.05</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">4.92</td>
    <td align="right">5.81</td>
    <td align="right">5.82</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.36</td>
    <td align="right">6.69</td>
    <td align="right">4.69</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">8.23</td>
    <td align="right">9.28</td>
    <td align="right">7.28</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">9.10</td>
    <td align="right">9.26</td>
    <td align="right">7.17</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">7.59</td>
    <td align="right">7.75</td>
    <td align="right">5.66</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">10.36</td>
    <td align="right">11.95</td>
    <td align="right">8.16</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">10.51</td>
    <td align="right">12.67</td>
    <td align="right">8.28</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">8.19</td>
    <td align="right">8.26</td>
    <td align="right">14.14</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.69</td>
    <td align="right">10.26</td>
    <td align="right">18.11</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">13.48</td>
    <td align="right">13.72</td>
    <td align="right">13.72</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.31</td>
    <td align="right">8.92</td>
    <td align="right">12.68</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">13.14</td>
    <td align="right">10.28</td>
    <td align="right">14.54</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">18.04</td>
    <td align="right">17.83</td>
    <td align="right">17.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">12.40</td>
    <td align="right">11.65</td>
    <td align="right">12.55</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">17.09</td>
    <td align="right">14.14</td>
    <td align="right">15.71</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">20.88</td>
    <td align="right">20.49</td>
    <td align="right">20.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">17.81</td>
    <td align="right">15.11</td>
    <td align="right">14.29</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">22.82</td>
    <td align="right">18.21</td>
    <td align="right">16.45</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">27.91</td>
    <td align="right">28.79</td>
    <td align="right">28.72</td>
  </tr>
</table>

<!--gcc-x64/comparison_table.cpp.txt-->

### Clang 18, x64
<!--clang-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">26.90</td>
    <td align="right">4.15</td>
    <td align="right">3.44</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">9.33</td>
    <td align="right">9.05</td>
    <td align="right">15.37</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.68</td>
    <td align="right">3.97</td>
    <td align="right">4.07</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.91</td>
    <td align="right">4.68</td>
    <td align="right">4.69</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">13.38</td>
    <td align="right">13.74</td>
    <td align="right">16.66</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">7.15</td>
    <td align="right">4.57</td>
    <td align="right">4.59</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.52</td>
    <td align="right">5.36</td>
    <td align="right">5.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">17.76</td>
    <td align="right">16.89</td>
    <td align="right">15.66</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.55</td>
    <td align="right">5.07</td>
    <td align="right">5.25</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.69</td>
    <td align="right">6.00</td>
    <td align="right">6.03</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">20.49</td>
    <td align="right">22.73</td>
    <td align="right">15.90</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">9.57</td>
    <td align="right">5.71</td>
    <td align="right">5.88</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">2.91</td>
    <td align="right">3.31</td>
    <td align="right">3.36</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">3.06</td>
    <td align="right">3.62</td>
    <td align="right">3.62</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">3.18</td>
    <td align="right">3.60</td>
    <td align="right">3.49</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.63</td>
    <td align="right">2.55</td>
    <td align="right">2.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.73</td>
    <td align="right">4.09</td>
    <td align="right">4.09</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.78</td>
    <td align="right">4.42</td>
    <td align="right">4.41</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.17</td>
    <td align="right">2.31</td>
    <td align="right">2.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">5.60</td>
    <td align="right">7.19</td>
    <td align="right">7.23</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">5.73</td>
    <td align="right">7.06</td>
    <td align="right">7.01</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">4.24</td>
    <td align="right">4.38</td>
    <td align="right">3.18</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">6.06</td>
    <td align="right">7.71</td>
    <td align="right">7.72</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">6.33</td>
    <td align="right">8.13</td>
    <td align="right">8.28</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">4.23</td>
    <td align="right">4.47</td>
    <td align="right">3.16</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.62</td>
    <td align="right">2.34</td>
    <td align="right">2.35</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">3.64</td>
    <td align="right">4.05</td>
    <td align="right">4.05</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">3.69</td>
    <td align="right">3.92</td>
    <td align="right">3.95</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.73</td>
    <td align="right">2.44</td>
    <td align="right">2.42</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">2.97</td>
    <td align="right">3.74</td>
    <td align="right">3.73</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">3.92</td>
    <td align="right">4.05</td>
    <td align="right">4.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">4.31</td>
    <td align="right">4.32</td>
    <td align="right">2.94</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">5.71</td>
    <td align="right">6.06</td>
    <td align="right">4.66</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">5.83</td>
    <td align="right">6.02</td>
    <td align="right">4.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">4.31</td>
    <td align="right">4.35</td>
    <td align="right">2.96</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">6.63</td>
    <td align="right">7.12</td>
    <td align="right">4.62</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">6.84</td>
    <td align="right">7.07</td>
    <td align="right">4.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.83</td>
    <td align="right">6.11</td>
    <td align="right">12.20</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.43</td>
    <td align="right">7.97</td>
    <td align="right">16.39</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">10.64</td>
    <td align="right">11.19</td>
    <td align="right">11.18</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">9.42</td>
    <td align="right">8.18</td>
    <td align="right">12.17</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">12.70</td>
    <td align="right">9.60</td>
    <td align="right">13.92</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">14.63</td>
    <td align="right">15.54</td>
    <td align="right">15.37</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">11.67</td>
    <td align="right">9.96</td>
    <td align="right">11.80</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">14.92</td>
    <td align="right">12.40</td>
    <td align="right">14.75</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">17.23</td>
    <td align="right">17.47</td>
    <td align="right">17.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">14.83</td>
    <td align="right">12.28</td>
    <td align="right">12.50</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">17.85</td>
    <td align="right">13.99</td>
    <td align="right">14.27</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">22.45</td>
    <td align="right">22.69</td>
    <td align="right">21.88</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">33.00</td>
    <td align="right">16.12</td>
    <td align="right">6.93</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">9.96</td>
    <td align="right">9.16</td>
    <td align="right">15.52</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">6.31</td>
    <td align="right">4.05</td>
    <td align="right">4.20</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">7.16</td>
    <td align="right">4.72</td>
    <td align="right">4.68</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">14.10</td>
    <td align="right">14.04</td>
    <td align="right">16.74</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">8.15</td>
    <td align="right">5.25</td>
    <td align="right">4.85</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">8.81</td>
    <td align="right">5.58</td>
    <td align="right">5.30</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">20.42</td>
    <td align="right">19.85</td>
    <td align="right">15.91</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">10.25</td>
    <td align="right">5.84</td>
    <td align="right">5.85</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">14.14</td>
    <td align="right">6.56</td>
    <td align="right">6.77</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">36.09</td>
    <td align="right">35.92</td>
    <td align="right">18.23</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">14.43</td>
    <td align="right">12.56</td>
    <td align="right">11.31</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">2.94</td>
    <td align="right">3.33</td>
    <td align="right">3.37</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">3.21</td>
    <td align="right">3.67</td>
    <td align="right">3.69</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">3.38</td>
    <td align="right">3.62</td>
    <td align="right">3.60</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">2.74</td>
    <td align="right">2.64</td>
    <td align="right">2.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.75</td>
    <td align="right">4.24</td>
    <td align="right">4.25</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.80</td>
    <td align="right">4.48</td>
    <td align="right">4.80</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">2.23</td>
    <td align="right">2.44</td>
    <td align="right">2.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">5.59</td>
    <td align="right">7.22</td>
    <td align="right">7.51</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">5.86</td>
    <td align="right">7.05</td>
    <td align="right">7.22</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">5.13</td>
    <td align="right">5.27</td>
    <td align="right">3.84</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">7.27</td>
    <td align="right">10.41</td>
    <td align="right">10.19</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">7.39</td>
    <td align="right">10.42</td>
    <td align="right">10.86</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">7.50</td>
    <td align="right">8.17</td>
    <td align="right">4.41</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">2.75</td>
    <td align="right">2.40</td>
    <td align="right">2.42</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">3.85</td>
    <td align="right">4.18</td>
    <td align="right">4.18</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">3.87</td>
    <td align="right">3.98</td>
    <td align="right">4.00</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">2.78</td>
    <td align="right">2.49</td>
    <td align="right">2.43</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">3.03</td>
    <td align="right">3.84</td>
    <td align="right">3.91</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">3.91</td>
    <td align="right">4.06</td>
    <td align="right">4.06</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">4.67</td>
    <td align="right">5.53</td>
    <td align="right">5.05</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">5.66</td>
    <td align="right">6.76</td>
    <td align="right">5.24</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">6.30</td>
    <td align="right">6.08</td>
    <td align="right">5.04</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">7.97</td>
    <td align="right">7.66</td>
    <td align="right">4.27</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">7.86</td>
    <td align="right">9.23</td>
    <td align="right">5.55</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">8.91</td>
    <td align="right">9.76</td>
    <td align="right">5.99</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">7.06</td>
    <td align="right">6.31</td>
    <td align="right">12.29</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.82</td>
    <td align="right">8.69</td>
    <td align="right">17.32</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">12.85</td>
    <td align="right">13.12</td>
    <td align="right">13.10</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">10.60</td>
    <td align="right">8.75</td>
    <td align="right">13.04</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">14.21</td>
    <td align="right">10.46</td>
    <td align="right">14.50</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">17.18</td>
    <td align="right">17.11</td>
    <td align="right">17.22</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">21.97</td>
    <td align="right">13.25</td>
    <td align="right">14.18</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">38.76</td>
    <td align="right">21.03</td>
    <td align="right">17.03</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">19.29</td>
    <td align="right">19.66</td>
    <td align="right">19.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">28.43</td>
    <td align="right">20.25</td>
    <td align="right">16.46</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">45.78</td>
    <td align="right">33.93</td>
    <td align="right">18.35</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">34.19</td>
    <td align="right">31.10</td>
    <td align="right">30.01</td>
  </tr>
</table>

<!--clang-x64/comparison_table.cpp.txt-->

### Clang 15, ARM64
<!--clang-arm64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">22.28</td>
    <td align="right">5.32</td>
    <td align="right">4.40</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">8.66</td>
    <td align="right">4.68</td>
    <td align="right">12.42</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">1.46</td>
    <td align="right">1.42</td>
    <td align="right">1.68</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">1.73</td>
    <td align="right">1.42</td>
    <td align="right">1.41</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">11.62</td>
    <td align="right">7.56</td>
    <td align="right">12.91</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">1.58</td>
    <td align="right">1.50</td>
    <td align="right">1.89</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">1.80</td>
    <td align="right">2.32</td>
    <td align="right">1.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">15.96</td>
    <td align="right">10.38</td>
    <td align="right">12.47</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">1.73</td>
    <td align="right">1.80</td>
    <td align="right">2.46</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">2.45</td>
    <td align="right">2.22</td>
    <td align="right">1.81</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">19.99</td>
    <td align="right">12.35</td>
    <td align="right">12.93</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">2.11</td>
    <td align="right">2.08</td>
    <td align="right">2.41</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">1.97</td>
    <td align="right">1.78</td>
    <td align="right">1.75</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.64</td>
    <td align="right">1.76</td>
    <td align="right">2.53</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.51</td>
    <td align="right">1.96</td>
    <td align="right">1.90</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">2.66</td>
    <td align="right">1.84</td>
    <td align="right">1.88</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.62</td>
    <td align="right">2.20</td>
    <td align="right">2.11</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.06</td>
    <td align="right">2.56</td>
    <td align="right">2.40</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">1.70</td>
    <td align="right">1.52</td>
    <td align="right">1.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.87</td>
    <td align="right">3.19</td>
    <td align="right">3.50</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.62</td>
    <td align="right">3.05</td>
    <td align="right">3.09</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">3.57</td>
    <td align="right">3.64</td>
    <td align="right">2.01</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">4.72</td>
    <td align="right">3.65</td>
    <td align="right">3.53</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">4.92</td>
    <td align="right">4.40</td>
    <td align="right">4.35</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">3.37</td>
    <td align="right">3.41</td>
    <td align="right">1.97</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">2.63</td>
    <td align="right">1.86</td>
    <td align="right">1.84</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">2.49</td>
    <td align="right">1.99</td>
    <td align="right">2.33</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">2.80</td>
    <td align="right">1.98</td>
    <td align="right">2.20</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">2.18</td>
    <td align="right">1.80</td>
    <td align="right">2.21</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">2.65</td>
    <td align="right">2.58</td>
    <td align="right">2.31</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">3.10</td>
    <td align="right">2.63</td>
    <td align="right">2.31</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">3.04</td>
    <td align="right">2.98</td>
    <td align="right">1.84</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">4.39</td>
    <td align="right">3.07</td>
    <td align="right">3.35</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">4.59</td>
    <td align="right">3.35</td>
    <td align="right">3.39</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">3.48</td>
    <td align="right">3.45</td>
    <td align="right">1.98</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">5.37</td>
    <td align="right">3.55</td>
    <td align="right">4.77</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">5.41</td>
    <td align="right">4.43</td>
    <td align="right">4.23</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">6.06</td>
    <td align="right">3.41</td>
    <td align="right">12.20</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">7.79</td>
    <td align="right">4.04</td>
    <td align="right">15.72</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">8.26</td>
    <td align="right">5.42</td>
    <td align="right">5.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">4.92</td>
    <td align="right">4.89</td>
    <td align="right">11.12</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">9.84</td>
    <td align="right">5.04</td>
    <td align="right">12.10</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">13.85</td>
    <td align="right">7.50</td>
    <td align="right">7.85</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">6.34</td>
    <td align="right">5.83</td>
    <td align="right">10.75</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">9.37</td>
    <td align="right">7.30</td>
    <td align="right">13.33</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">12.08</td>
    <td align="right">7.69</td>
    <td align="right">8.10</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">10.57</td>
    <td align="right">7.52</td>
    <td align="right">12.86</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">11.60</td>
    <td align="right">7.31</td>
    <td align="right">13.55</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">18.33</td>
    <td align="right">11.77</td>
    <td align="right">11.91</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">29.11</td>
    <td align="right">16.11</td>
    <td align="right">11.88</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">12.13</td>
    <td align="right">13.80</td>
    <td align="right">21.20</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">5.72</td>
    <td align="right">2.21</td>
    <td align="right">4.54</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">3.08</td>
    <td align="right">3.63</td>
    <td align="right">5.38</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">24.27</td>
    <td align="right">22.84</td>
    <td align="right">24.24</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">7.71</td>
    <td align="right">6.79</td>
    <td align="right">6.39</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">7.51</td>
    <td align="right">7.79</td>
    <td align="right">8.10</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">50.09</td>
    <td align="right">42.64</td>
    <td align="right">27.40</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">12.20</td>
    <td align="right">10.12</td>
    <td align="right">11.35</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">14.04</td>
    <td align="right">12.02</td>
    <td align="right">13.00</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">96.59</td>
    <td align="right">64.44</td>
    <td align="right">31.71</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">14.39</td>
    <td align="right">13.84</td>
    <td align="right">12.69</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">13.53</td>
    <td align="right">11.86</td>
    <td align="right">10.59</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">4.90</td>
    <td align="right">6.05</td>
    <td align="right">5.14</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">4.63</td>
    <td align="right">5.32</td>
    <td align="right">5.52</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.75</td>
    <td align="right">7.12</td>
    <td align="right">6.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">9.54</td>
    <td align="right">10.08</td>
    <td align="right">10.15</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">12.38</td>
    <td align="right">11.80</td>
    <td align="right">11.50</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">7.85</td>
    <td align="right">9.01</td>
    <td align="right">8.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">23.01</td>
    <td align="right">18.22</td>
    <td align="right">19.56</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">22.80</td>
    <td align="right">16.91</td>
    <td align="right">19.28</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">16.41</td>
    <td align="right">11.55</td>
    <td align="right">9.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">19.17</td>
    <td align="right">17.44</td>
    <td align="right">15.39</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">17.51</td>
    <td align="right">19.81</td>
    <td align="right">21.20</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">14.56</td>
    <td align="right">16.86</td>
    <td align="right">9.14</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">5.25</td>
    <td align="right">5.56</td>
    <td align="right">5.09</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">5.13</td>
    <td align="right">4.63</td>
    <td align="right">4.84</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">4.81</td>
    <td align="right">5.21</td>
    <td align="right">5.02</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">6.85</td>
    <td align="right">9.30</td>
    <td align="right">8.78</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">8.06</td>
    <td align="right">7.39</td>
    <td align="right">6.91</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">7.55</td>
    <td align="right">12.31</td>
    <td align="right">10.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">11.82</td>
    <td align="right">10.65</td>
    <td align="right">7.25</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">14.31</td>
    <td align="right">10.41</td>
    <td align="right">10.78</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">10.88</td>
    <td align="right">8.92</td>
    <td align="right">9.28</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">9.91</td>
    <td align="right">10.99</td>
    <td align="right">6.55</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">16.78</td>
    <td align="right">13.72</td>
    <td align="right">14.28</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">15.83</td>
    <td align="right">14.63</td>
    <td align="right">15.81</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">5.06</td>
    <td align="right">4.53</td>
    <td align="right">12.20</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">9.96</td>
    <td align="right">5.23</td>
    <td align="right">15.09</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">10.38</td>
    <td align="right">8.99</td>
    <td align="right">10.32</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">17.71</td>
    <td align="right">13.85</td>
    <td align="right">16.23</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">16.42</td>
    <td align="right">8.74</td>
    <td align="right">13.54</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">17.68</td>
    <td align="right">14.28</td>
    <td align="right">14.81</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">19.79</td>
    <td align="right">13.85</td>
    <td align="right">14.52</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">29.66</td>
    <td align="right">20.00</td>
    <td align="right">16.47</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">25.86</td>
    <td align="right">25.37</td>
    <td align="right">27.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">24.86</td>
    <td align="right">19.88</td>
    <td align="right">16.27</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">30.96</td>
    <td align="right">22.58</td>
    <td align="right">18.99</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">43.45</td>
    <td align="right">40.17</td>
    <td align="right">44.16</td>
  </tr>
</table>

<!--clang-arm64/comparison_table.cpp.txt-->

### VS 2022, x64
<!--vs-x64/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">35.09</td>
    <td align="right">5.78</td>
    <td align="right">3.67</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1635</td>
    <td align="right">12.07</td>
    <td align="right">12.50</td>
    <td align="right">17.04</td>
    <td align="center">4</td>
    <td align="right">3.3525</td>
    <td align="right">5.89</td>
    <td align="right">4.22</td>
    <td align="right">4.22</td>
    <td align="center">5</td>
    <td align="right">3.0203</td>
    <td align="right">6.96</td>
    <td align="right">5.26</td>
    <td align="right">5.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3151</td>
    <td align="right">18.63</td>
    <td align="right">17.95</td>
    <td align="right">17.74</td>
    <td align="center">5</td>
    <td align="right">1.0369</td>
    <td align="right">7.08</td>
    <td align="right">4.85</td>
    <td align="right">4.73</td>
    <td align="center">6</td>
    <td align="right">0.8293</td>
    <td align="right">8.03</td>
    <td align="right">5.96</td>
    <td align="right">5.94</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">23.71</td>
    <td align="right">21.55</td>
    <td align="right">16.84</td>
    <td align="center">6</td>
    <td align="right">0.4138</td>
    <td align="right">8.73</td>
    <td align="right">5.39</td>
    <td align="right">5.35</td>
    <td align="center">7</td>
    <td align="right">0.2824</td>
    <td align="right">9.44</td>
    <td align="right">6.66</td>
    <td align="right">6.71</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0084</td>
    <td align="right">31.51</td>
    <td align="right">27.39</td>
    <td align="right">17.61</td>
    <td align="center">7</td>
    <td align="right">0.1936</td>
    <td align="right">10.04</td>
    <td align="right">5.99</td>
    <td align="right">5.96</td>
    <td align="center">8</td>
    <td align="right">0.1197</td>
    <td align="right">10.53</td>
    <td align="right">7.50</td>
    <td align="right">7.70</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4274</td>
    <td align="right">7.89</td>
    <td align="right">5.60</td>
    <td align="right">5.58</td>
    <td align="center">5</td>
    <td align="right">2.3232</td>
    <td align="right">9.16</td>
    <td align="right">5.65</td>
    <td align="right">5.60</td>
    <td align="center">5</td>
    <td align="right">2.7402</td>
    <td align="right">3.36</td>
    <td align="right">3.98</td>
    <td align="right">4.09</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">11.74</td>
    <td align="right">8.23</td>
    <td align="right">8.25</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">16.33</td>
    <td align="right">8.83</td>
    <td align="right">7.95</td>
    <td align="center">8</td>
    <td align="right">0.5360</td>
    <td align="right">2.89</td>
    <td align="right">4.87</td>
    <td align="right">4.12</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0782</td>
    <td align="right">15.08</td>
    <td align="right">11.09</td>
    <td align="right">11.00</td>
    <td align="center">11</td>
    <td align="right">0.0581</td>
    <td align="right">24.42</td>
    <td align="right">10.67</td>
    <td align="right">10.72</td>
    <td align="center">11</td>
    <td align="right">0.1169</td>
    <td align="right">5.11</td>
    <td align="right">7.31</td>
    <td align="right">5.51</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0132</td>
    <td align="right">16.98</td>
    <td align="right">12.49</td>
    <td align="right">12.65</td>
    <td align="center">14</td>
    <td align="right">0.0131</td>
    <td align="right">22.16</td>
    <td align="right">13.91</td>
    <td align="right">13.85</td>
    <td align="center">13</td>
    <td align="right">0.0280</td>
    <td align="right">5.20</td>
    <td align="right">7.21</td>
    <td align="right">5.48</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4803</td>
    <td align="right">3.33</td>
    <td align="right">3.91</td>
    <td align="right">3.96</td>
    <td align="center">5</td>
    <td align="right">2.4404</td>
    <td align="right">4.60</td>
    <td align="right">5.53</td>
    <td align="right">5.50</td>
    <td align="center">5</td>
    <td align="right">2.3234</td>
    <td align="right">4.68</td>
    <td align="right">5.49</td>
    <td align="right">5.53</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4455</td>
    <td align="right">3.41</td>
    <td align="right">5.60</td>
    <td align="right">4.74</td>
    <td align="center">8</td>
    <td align="right">0.4197</td>
    <td align="right">4.77</td>
    <td align="right">5.84</td>
    <td align="right">5.03</td>
    <td align="center">8</td>
    <td align="right">0.3827</td>
    <td align="right">7.06</td>
    <td align="right">7.26</td>
    <td align="right">6.41</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0840</td>
    <td align="right">5.19</td>
    <td align="right">6.92</td>
    <td align="right">5.17</td>
    <td align="center">11</td>
    <td align="right">0.0761</td>
    <td align="right">9.93</td>
    <td align="right">9.50</td>
    <td align="right">7.67</td>
    <td align="center">11</td>
    <td align="right">0.0629</td>
    <td align="right">9.67</td>
    <td align="right">9.39</td>
    <td align="right">7.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">5.16</td>
    <td align="right">6.84</td>
    <td align="right">5.08</td>
    <td align="center">13</td>
    <td align="right">0.0154</td>
    <td align="right">10.38</td>
    <td align="right">10.99</td>
    <td align="right">7.96</td>
    <td align="center">14</td>
    <td align="right">0.0121</td>
    <td align="right">10.25</td>
    <td align="right">10.75</td>
    <td align="right">7.57</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.2994</td>
    <td align="right">8.58</td>
    <td align="right">8.68</td>
    <td align="right">13.69</td>
    <td align="center">6</td>
    <td align="right">2.2649</td>
    <td align="right">12.31</td>
    <td align="right">11.78</td>
    <td align="right">17.15</td>
    <td align="center">7</td>
    <td align="right">2.3451</td>
    <td align="right">12.84</td>
    <td align="right">10.86</td>
    <td align="right">10.91</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4106</td>
    <td align="right">11.83</td>
    <td align="right">11.20</td>
    <td align="right">13.00</td>
    <td align="center">7</td>
    <td align="right">0.3873</td>
    <td align="right">13.43</td>
    <td align="right">13.05</td>
    <td align="right">14.55</td>
    <td align="center">10</td>
    <td align="right">0.3354</td>
    <td align="right">18.77</td>
    <td align="right">17.55</td>
    <td align="right">17.57</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0845</td>
    <td align="right">14.36</td>
    <td align="right">14.27</td>
    <td align="right">12.70</td>
    <td align="center">10</td>
    <td align="right">0.0708</td>
    <td align="right">19.48</td>
    <td align="right">17.79</td>
    <td align="right">15.41</td>
    <td align="center">11</td>
    <td align="right">0.0510</td>
    <td align="right">22.14</td>
    <td align="right">18.55</td>
    <td align="right">18.92</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0198</td>
    <td align="right">19.64</td>
    <td align="right">17.61</td>
    <td align="right">14.01</td>
    <td align="center">12</td>
    <td align="right">0.0147</td>
    <td align="right">20.67</td>
    <td align="right">20.59</td>
    <td align="right">14.81</td>
    <td align="center">15</td>
    <td align="right">0.0087</td>
    <td align="right">30.40</td>
    <td align="right">28.23</td>
    <td align="right">28.13</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">42.80</td>
    <td align="right">20.78</td>
    <td align="right">7.26</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1566</td>
    <td align="right">14.87</td>
    <td align="right">15.68</td>
    <td align="right">17.86</td>
    <td align="center">4</td>
    <td align="right">3.3462</td>
    <td align="right">7.84</td>
    <td align="right">4.82</td>
    <td align="right">4.50</td>
    <td align="center">5</td>
    <td align="right">3.0448</td>
    <td align="right">8.68</td>
    <td align="right">5.73</td>
    <td align="right">5.58</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3146</td>
    <td align="right">30.20</td>
    <td align="right">23.86</td>
    <td align="right">19.73</td>
    <td align="center">5</td>
    <td align="right">1.0310</td>
    <td align="right">10.54</td>
    <td align="right">7.85</td>
    <td align="right">6.25</td>
    <td align="center">6</td>
    <td align="right">0.8244</td>
    <td align="right">9.68</td>
    <td align="right">7.58</td>
    <td align="right">6.52</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0456</td>
    <td align="right">33.82</td>
    <td align="right">26.85</td>
    <td align="right">21.02</td>
    <td align="center">6</td>
    <td align="right">0.4035</td>
    <td align="right">13.18</td>
    <td align="right">6.59</td>
    <td align="right">6.45</td>
    <td align="center">7</td>
    <td align="right">0.2885</td>
    <td align="right">11.92</td>
    <td align="right">12.01</td>
    <td align="right">10.02</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0066</td>
    <td align="right">61.84</td>
    <td align="right">52.37</td>
    <td align="right">20.63</td>
    <td align="center">7</td>
    <td align="right">0.1879</td>
    <td align="right">14.36</td>
    <td align="right">9.47</td>
    <td align="right">9.20</td>
    <td align="center">8</td>
    <td align="right">0.1185</td>
    <td align="right">15.78</td>
    <td align="right">13.44</td>
    <td align="right">12.89</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4515</td>
    <td align="right">9.35</td>
    <td align="right">6.26</td>
    <td align="right">6.29</td>
    <td align="center">5</td>
    <td align="right">2.3208</td>
    <td align="right">9.43</td>
    <td align="right">6.35</td>
    <td align="right">6.41</td>
    <td align="center">5</td>
    <td align="right">2.7234</td>
    <td align="right">3.88</td>
    <td align="right">4.45</td>
    <td align="right">4.42</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4244</td>
    <td align="right">15.64</td>
    <td align="right">10.77</td>
    <td align="right">11.24</td>
    <td align="center">8</td>
    <td align="right">0.3758</td>
    <td align="right">18.74</td>
    <td align="right">9.87</td>
    <td align="right">9.42</td>
    <td align="center">8</td>
    <td align="right">0.5407</td>
    <td align="right">3.25</td>
    <td align="right">5.26</td>
    <td align="right">4.53</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0776</td>
    <td align="right">18.35</td>
    <td align="right">13.62</td>
    <td align="right">13.99</td>
    <td align="center">11</td>
    <td align="right">0.0641</td>
    <td align="right">27.41</td>
    <td align="right">12.72</td>
    <td align="right">13.04</td>
    <td align="center">11</td>
    <td align="right">0.1174</td>
    <td align="right">7.46</td>
    <td align="right">8.73</td>
    <td align="right">6.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0148</td>
    <td align="right">23.66</td>
    <td align="right">17.89</td>
    <td align="right">16.39</td>
    <td align="center">14</td>
    <td align="right">0.0120</td>
    <td align="right">28.08</td>
    <td align="right">18.10</td>
    <td align="right">18.42</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">9.17</td>
    <td align="right">12.81</td>
    <td align="right">10.51</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4625</td>
    <td align="right">3.67</td>
    <td align="right">4.17</td>
    <td align="right">4.58</td>
    <td align="center">5</td>
    <td align="right">2.4388</td>
    <td align="right">5.01</td>
    <td align="right">5.96</td>
    <td align="right">5.92</td>
    <td align="center">5</td>
    <td align="right">2.3198</td>
    <td align="right">5.15</td>
    <td align="right">5.77</td>
    <td align="right">5.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4428</td>
    <td align="right">3.68</td>
    <td align="right">5.99</td>
    <td align="right">5.22</td>
    <td align="center">8</td>
    <td align="right">0.4190</td>
    <td align="right">5.26</td>
    <td align="right">6.55</td>
    <td align="right">5.61</td>
    <td align="center">8</td>
    <td align="right">0.3747</td>
    <td align="right">8.69</td>
    <td align="right">7.66</td>
    <td align="right">6.76</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0866</td>
    <td align="right">6.05</td>
    <td align="right">9.27</td>
    <td align="right">6.08</td>
    <td align="center">11</td>
    <td align="right">0.0781</td>
    <td align="right">12.30</td>
    <td align="right">12.15</td>
    <td align="right">8.50</td>
    <td align="center">11</td>
    <td align="right">0.0651</td>
    <td align="right">11.19</td>
    <td align="right">11.16</td>
    <td align="right">8.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0180</td>
    <td align="right">10.58</td>
    <td align="right">10.68</td>
    <td align="right">8.26</td>
    <td align="center">13</td>
    <td align="right">0.0147</td>
    <td align="right">13.05</td>
    <td align="right">16.43</td>
    <td align="right">10.32</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">12.96</td>
    <td align="right">14.36</td>
    <td align="right">10.14</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3301</td>
    <td align="right">9.74</td>
    <td align="right">9.71</td>
    <td align="right">14.05</td>
    <td align="center">6</td>
    <td align="right">2.2943</td>
    <td align="right">12.90</td>
    <td align="right">12.77</td>
    <td align="right">18.00</td>
    <td align="center">7</td>
    <td align="right">2.3317</td>
    <td align="right">18.12</td>
    <td align="right">16.42</td>
    <td align="right">16.46</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4128</td>
    <td align="right">14.30</td>
    <td align="right">14.85</td>
    <td align="right">14.12</td>
    <td align="center">7</td>
    <td align="right">0.3893</td>
    <td align="right">15.39</td>
    <td align="right">15.12</td>
    <td align="right">15.08</td>
    <td align="center">10</td>
    <td align="right">0.3489</td>
    <td align="right">23.93</td>
    <td align="right">22.33</td>
    <td align="right">22.73</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0838</td>
    <td align="right">17.69</td>
    <td align="right">18.28</td>
    <td align="right">13.96</td>
    <td align="center">10</td>
    <td align="right">0.0718</td>
    <td align="right">23.76</td>
    <td align="right">22.48</td>
    <td align="right">19.09</td>
    <td align="center">11</td>
    <td align="right">0.0492</td>
    <td align="right">31.91</td>
    <td align="right">27.89</td>
    <td align="right">28.70</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0197</td>
    <td align="right">28.74</td>
    <td align="right">25.63</td>
    <td align="right">16.54</td>
    <td align="center">12</td>
    <td align="right">0.0151</td>
    <td align="right">32.82</td>
    <td align="right">32.19</td>
    <td align="right">18.91</td>
    <td align="center">15</td>
    <td align="right">0.0076</td>
    <td align="right">40.38</td>
    <td align="right">43.55</td>
    <td align="right">39.65</td>
  </tr>
</table>

<!--vs-x64/comparison_table.cpp.txt-->

### GCC 14, x86
<!--gcc-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">62.94</td>
    <td align="right">32.44</td>
    <td align="right">15.41</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">27.79</td>
    <td align="right">41.94</td>
    <td align="right">36.05</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">12.76</td>
    <td align="right">15.67</td>
    <td align="right">15.71</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">16.13</td>
    <td align="right">19.18</td>
    <td align="right">19.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">37.43</td>
    <td align="right">64.15</td>
    <td align="right">39.14</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">17.28</td>
    <td align="right">19.60</td>
    <td align="right">19.63</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">16.05</td>
    <td align="right">18.59</td>
    <td align="right">18.79</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">44.96</td>
    <td align="right">77.57</td>
    <td align="right">38.46</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">17.49</td>
    <td align="right">18.77</td>
    <td align="right">18.78</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">18.14</td>
    <td align="right">18.57</td>
    <td align="right">18.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">57.51</td>
    <td align="right">98.01</td>
    <td align="right">37.36</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">18.47</td>
    <td align="right">18.85</td>
    <td align="right">18.80</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">18.92</td>
    <td align="right">20.02</td>
    <td align="right">19.83</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.65</td>
    <td align="right">21.48</td>
    <td align="right">21.41</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.33</td>
    <td align="right">22.20</td>
    <td align="right">22.14</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">10.93</td>
    <td align="right">13.84</td>
    <td align="right">13.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">20.99</td>
    <td align="right">26.09</td>
    <td align="right">26.07</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">39.47</td>
    <td align="right">27.98</td>
    <td align="right">28.04</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">13.04</td>
    <td align="right">16.41</td>
    <td align="right">15.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.39</td>
    <td align="right">33.62</td>
    <td align="right">33.25</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">65.21</td>
    <td align="right">47.11</td>
    <td align="right">47.08</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">15.19</td>
    <td align="right">19.73</td>
    <td align="right">19.68</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.95</td>
    <td align="right">36.09</td>
    <td align="right">35.82</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">77.96</td>
    <td align="right">56.30</td>
    <td align="right">56.42</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">22.74</td>
    <td align="right">25.39</td>
    <td align="right">25.45</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">15.19</td>
    <td align="right">15.48</td>
    <td align="right">15.48</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">16.09</td>
    <td align="right">21.21</td>
    <td align="right">21.19</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">30.29</td>
    <td align="right">22.08</td>
    <td align="right">22.08</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">19.69</td>
    <td align="right">20.59</td>
    <td align="right">20.56</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">21.09</td>
    <td align="right">26.00</td>
    <td align="right">26.06</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">40.06</td>
    <td align="right">28.18</td>
    <td align="right">28.17</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">27.71</td>
    <td align="right">24.94</td>
    <td align="right">25.04</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.42</td>
    <td align="right">33.73</td>
    <td align="right">33.74</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">65.43</td>
    <td align="right">47.23</td>
    <td align="right">47.52</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">35.20</td>
    <td align="right">37.43</td>
    <td align="right">37.46</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">34.46</td>
    <td align="right">36.11</td>
    <td align="right">36.25</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">78.36</td>
    <td align="right">56.95</td>
    <td align="right">56.71</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">17.40</td>
    <td align="right">21.06</td>
    <td align="right">25.44</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.23</td>
    <td align="right">29.54</td>
    <td align="right">34.66</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">27.76</td>
    <td align="right">30.22</td>
    <td align="right">30.16</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">27.28</td>
    <td align="right">28.21</td>
    <td align="right">26.11</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">38.61</td>
    <td align="right">33.25</td>
    <td align="right">30.46</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">37.17</td>
    <td align="right">38.18</td>
    <td align="right">38.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">32.51</td>
    <td align="right">33.62</td>
    <td align="right">25.76</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">47.19</td>
    <td align="right">42.35</td>
    <td align="right">33.80</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">39.78</td>
    <td align="right">41.75</td>
    <td align="right">41.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">37.52</td>
    <td align="right">40.35</td>
    <td align="right">26.98</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">48.80</td>
    <td align="right">44.14</td>
    <td align="right">31.59</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">54.50</td>
    <td align="right">58.79</td>
    <td align="right">58.95</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">86.17</td>
    <td align="right">115.30</td>
    <td align="right">28.51</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">29.27</td>
    <td align="right">48.58</td>
    <td align="right">42.09</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">14.56</td>
    <td align="right">21.25</td>
    <td align="right">18.04</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">17.22</td>
    <td align="right">26.87</td>
    <td align="right">23.14</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">65.47</td>
    <td align="right">81.78</td>
    <td align="right">52.10</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">23.14</td>
    <td align="right">36.40</td>
    <td align="right">43.92</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">32.41</td>
    <td align="right">28.75</td>
    <td align="right">39.56</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">125.92</td>
    <td align="right">213.66</td>
    <td align="right">83.89</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">23.39</td>
    <td align="right">30.84</td>
    <td align="right">40.79</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">23.56</td>
    <td align="right">23.76</td>
    <td align="right">20.63</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">158.85</td>
    <td align="right">327.20</td>
    <td align="right">114.92</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">47.72</td>
    <td align="right">35.93</td>
    <td align="right">29.75</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">36.41</td>
    <td align="right">44.20</td>
    <td align="right">41.75</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">17.09</td>
    <td align="right">22.56</td>
    <td align="right">22.49</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">34.14</td>
    <td align="right">23.52</td>
    <td align="right">23.55</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">11.35</td>
    <td align="right">14.18</td>
    <td align="right">14.22</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">26.31</td>
    <td align="right">32.21</td>
    <td align="right">34.47</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">87.93</td>
    <td align="right">69.29</td>
    <td align="right">75.55</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">34.81</td>
    <td align="right">38.91</td>
    <td align="right">32.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">87.52</td>
    <td align="right">97.75</td>
    <td align="right">98.38</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">109.13</td>
    <td align="right">92.50</td>
    <td align="right">103.20</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">49.39</td>
    <td align="right">56.05</td>
    <td align="right">56.26</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">95.95</td>
    <td align="right">70.66</td>
    <td align="right">69.38</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">132.61</td>
    <td align="right">112.85</td>
    <td align="right">117.59</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">64.96</td>
    <td align="right">86.90</td>
    <td align="right">87.56</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">24.94</td>
    <td align="right">22.03</td>
    <td align="right">22.62</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">27.56</td>
    <td align="right">34.60</td>
    <td align="right">35.22</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">70.64</td>
    <td align="right">39.14</td>
    <td align="right">37.94</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">47.16</td>
    <td align="right">41.15</td>
    <td align="right">39.19</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">31.94</td>
    <td align="right">27.13</td>
    <td align="right">29.31</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">55.95</td>
    <td align="right">31.50</td>
    <td align="right">29.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">56.45</td>
    <td align="right">56.80</td>
    <td align="right">58.63</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">45.90</td>
    <td align="right">64.93</td>
    <td align="right">79.39</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">70.53</td>
    <td align="right">51.63</td>
    <td align="right">50.38</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">44.38</td>
    <td align="right">48.23</td>
    <td align="right">50.47</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">37.58</td>
    <td align="right">40.87</td>
    <td align="right">52.29</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">92.15</td>
    <td align="right">62.49</td>
    <td align="right">61.80</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">17.64</td>
    <td align="right">21.55</td>
    <td align="right">26.20</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">32.90</td>
    <td align="right">29.72</td>
    <td align="right">36.23</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">29.65</td>
    <td align="right">32.80</td>
    <td align="right">32.79</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">28.59</td>
    <td align="right">29.08</td>
    <td align="right">26.83</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">39.27</td>
    <td align="right">34.25</td>
    <td align="right">30.91</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">40.10</td>
    <td align="right">40.45</td>
    <td align="right">41.45</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">33.60</td>
    <td align="right">33.88</td>
    <td align="right">26.41</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">51.14</td>
    <td align="right">51.52</td>
    <td align="right">35.06</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">41.41</td>
    <td align="right">43.20</td>
    <td align="right">43.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">41.70</td>
    <td align="right">46.40</td>
    <td align="right">28.92</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">60.21</td>
    <td align="right">58.49</td>
    <td align="right">44.47</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">60.96</td>
    <td align="right">74.34</td>
    <td align="right">74.40</td>
  </tr>
</table>

<!--gcc-x86/comparison_table.cpp.txt-->

### Clang 18, x86
<!--clang-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">63.36</td>
    <td align="right">11.01</td>
    <td align="right">7.97</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">14.16</td>
    <td align="right">23.12</td>
    <td align="right">26.64</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">10.33</td>
    <td align="right">12.41</td>
    <td align="right">12.38</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">28.70</td>
    <td align="right">13.84</td>
    <td align="right">13.85</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">19.57</td>
    <td align="right">35.42</td>
    <td align="right">29.23</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">31.16</td>
    <td align="right">14.08</td>
    <td align="right">14.06</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">14.91</td>
    <td align="right">15.40</td>
    <td align="right">15.32</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">25.04</td>
    <td align="right">47.33</td>
    <td align="right">29.36</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">14.76</td>
    <td align="right">15.48</td>
    <td align="right">15.45</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">16.28</td>
    <td align="right">17.15</td>
    <td align="right">16.75</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">31.35</td>
    <td align="right">60.35</td>
    <td align="right">31.19</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">16.20</td>
    <td align="right">16.30</td>
    <td align="right">16.29</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">17.29</td>
    <td align="right">17.83</td>
    <td align="right">17.83</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.67</td>
    <td align="right">16.04</td>
    <td align="right">16.05</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.30</td>
    <td align="right">16.71</td>
    <td align="right">16.69</td>
    <td align="center">5</td>
    <td align="right">2.7635</td>
    <td align="right">7.00</td>
    <td align="right">9.34</td>
    <td align="right">9.34</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.36</td>
    <td align="right">22.53</td>
    <td align="right">22.59</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.78</td>
    <td align="right">22.36</td>
    <td align="right">22.35</td>
    <td align="center">8</td>
    <td align="right">0.5186</td>
    <td align="right">11.18</td>
    <td align="right">14.06</td>
    <td align="right">13.88</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">23.80</td>
    <td align="right">32.11</td>
    <td align="right">32.04</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.54</td>
    <td align="right">30.73</td>
    <td align="right">30.63</td>
    <td align="center">11</td>
    <td align="right">0.1230</td>
    <td align="right">13.16</td>
    <td align="right">17.55</td>
    <td align="right">17.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.86</td>
    <td align="right">35.63</td>
    <td align="right">35.68</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.23</td>
    <td align="right">35.73</td>
    <td align="right">35.68</td>
    <td align="center">13</td>
    <td align="right">0.0295</td>
    <td align="right">16.26</td>
    <td align="right">20.54</td>
    <td align="right">20.46</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4627</td>
    <td align="right">6.55</td>
    <td align="right">9.35</td>
    <td align="right">9.31</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">12.67</td>
    <td align="right">16.04</td>
    <td align="right">16.06</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">13.30</td>
    <td align="right">16.67</td>
    <td align="right">16.70</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4575</td>
    <td align="right">11.04</td>
    <td align="right">13.69</td>
    <td align="right">13.67</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">17.39</td>
    <td align="right">22.51</td>
    <td align="right">22.54</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">17.78</td>
    <td align="right">22.42</td>
    <td align="right">22.35</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0876</td>
    <td align="right">12.25</td>
    <td align="right">17.61</td>
    <td align="right">17.63</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">24.02</td>
    <td align="right">32.04</td>
    <td align="right">32.04</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">25.58</td>
    <td align="right">30.75</td>
    <td align="right">30.64</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0171</td>
    <td align="right">16.13</td>
    <td align="right">20.95</td>
    <td align="right">20.99</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">26.86</td>
    <td align="right">35.64</td>
    <td align="right">35.66</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">33.14</td>
    <td align="right">35.76</td>
    <td align="right">35.70</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">13.15</td>
    <td align="right">16.15</td>
    <td align="right">19.88</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">48.46</td>
    <td align="right">33.29</td>
    <td align="right">36.63</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">20.39</td>
    <td align="right">23.98</td>
    <td align="right">23.99</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">19.69</td>
    <td align="right">23.36</td>
    <td align="right">20.66</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">54.33</td>
    <td align="right">37.21</td>
    <td align="right">35.58</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">27.17</td>
    <td align="right">31.50</td>
    <td align="right">31.50</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">23.94</td>
    <td align="right">29.78</td>
    <td align="right">20.59</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">59.84</td>
    <td align="right">45.41</td>
    <td align="right">37.68</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">30.08</td>
    <td align="right">35.27</td>
    <td align="right">35.36</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">29.82</td>
    <td align="right">35.44</td>
    <td align="right">21.35</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">65.25</td>
    <td align="right">47.75</td>
    <td align="right">36.81</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">41.64</td>
    <td align="right">46.02</td>
    <td align="right">45.86</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">77.95</td>
    <td align="right">44.65</td>
    <td align="right">10.56</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">14.11</td>
    <td align="right">22.84</td>
    <td align="right">28.21</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">10.54</td>
    <td align="right">12.57</td>
    <td align="right">12.62</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">29.57</td>
    <td align="right">14.04</td>
    <td align="right">14.03</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">19.33</td>
    <td align="right">34.23</td>
    <td align="right">29.72</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">31.73</td>
    <td align="right">13.81</td>
    <td align="right">14.15</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">14.45</td>
    <td align="right">15.03</td>
    <td align="right">15.16</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">26.62</td>
    <td align="right">52.17</td>
    <td align="right">36.30</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">25.13</td>
    <td align="right">19.56</td>
    <td align="right">22.17</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">19.71</td>
    <td align="right">21.05</td>
    <td align="right">20.19</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">56.66</td>
    <td align="right">103.09</td>
    <td align="right">50.89</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">38.01</td>
    <td align="right">29.82</td>
    <td align="right">39.82</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">43.92</td>
    <td align="right">48.23</td>
    <td align="right">47.89</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">13.94</td>
    <td align="right">17.79</td>
    <td align="right">17.99</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">17.11</td>
    <td align="right">21.54</td>
    <td align="right">20.46</td>
    <td align="center">5</td>
    <td align="right">2.7396</td>
    <td align="right">7.59</td>
    <td align="right">9.91</td>
    <td align="right">9.64</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">24.47</td>
    <td align="right">25.19</td>
    <td align="right">23.66</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">17.95</td>
    <td align="right">24.27</td>
    <td align="right">21.76</td>
    <td align="center">8</td>
    <td align="right">0.5422</td>
    <td align="right">11.04</td>
    <td align="right">13.97</td>
    <td align="right">13.78</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">29.48</td>
    <td align="right">41.17</td>
    <td align="right">50.37</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">26.72</td>
    <td align="right">34.57</td>
    <td align="right">34.85</td>
    <td align="center">11</td>
    <td align="right">0.1202</td>
    <td align="right">14.07</td>
    <td align="right">18.17</td>
    <td align="right">19.24</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">50.51</td>
    <td align="right">52.31</td>
    <td align="right">40.18</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">37.51</td>
    <td align="right">39.81</td>
    <td align="right">38.83</td>
    <td align="center">13</td>
    <td align="right">0.0273</td>
    <td align="right">20.23</td>
    <td align="right">27.89</td>
    <td align="right">25.19</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4723</td>
    <td align="right">6.72</td>
    <td align="right">9.53</td>
    <td align="right">9.51</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">12.75</td>
    <td align="right">16.56</td>
    <td align="right">16.61</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">13.36</td>
    <td align="right">17.46</td>
    <td align="right">17.48</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4399</td>
    <td align="right">11.66</td>
    <td align="right">13.46</td>
    <td align="right">13.34</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">16.94</td>
    <td align="right">21.85</td>
    <td align="right">22.01</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">17.98</td>
    <td align="right">23.15</td>
    <td align="right">21.99</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0859</td>
    <td align="right">13.13</td>
    <td align="right">17.12</td>
    <td align="right">17.96</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">25.07</td>
    <td align="right">33.65</td>
    <td align="right">34.02</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">26.20</td>
    <td align="right">32.03</td>
    <td align="right">31.30</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0182</td>
    <td align="right">25.32</td>
    <td align="right">25.60</td>
    <td align="right">24.93</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">37.60</td>
    <td align="right">47.01</td>
    <td align="right">54.16</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">37.05</td>
    <td align="right">38.58</td>
    <td align="right">37.53</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">13.34</td>
    <td align="right">16.70</td>
    <td align="right">21.08</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">52.37</td>
    <td align="right">34.17</td>
    <td align="right">37.09</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">21.91</td>
    <td align="right">25.90</td>
    <td align="right">25.87</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">19.88</td>
    <td align="right">23.30</td>
    <td align="right">20.61</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">56.14</td>
    <td align="right">36.61</td>
    <td align="right">35.75</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">28.92</td>
    <td align="right">33.06</td>
    <td align="right">33.23</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">28.31</td>
    <td align="right">39.65</td>
    <td align="right">21.70</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">82.65</td>
    <td align="right">61.96</td>
    <td align="right">50.36</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">32.40</td>
    <td align="right">36.68</td>
    <td align="right">36.15</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">38.49</td>
    <td align="right">58.00</td>
    <td align="right">32.95</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">91.83</td>
    <td align="right">70.16</td>
    <td align="right">44.14</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">44.30</td>
    <td align="right">48.66</td>
    <td align="right">49.38</td>
  </tr>
</table>

<!--clang-x86/comparison_table.cpp.txt-->

### VS 2022, x86
<!--vs-x86/comparison_table.cpp.txt-->

#### `N` = 1M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">42.70</td>
    <td align="right">8.50</td>
    <td align="right">6.65</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1546</td>
    <td align="right">59.39</td>
    <td align="right">54.63</td>
    <td align="right">41.41</td>
    <td align="center">4</td>
    <td align="right">3.3200</td>
    <td align="right">21.00</td>
    <td align="right">19.81</td>
    <td align="right">23.34</td>
    <td align="center">5</td>
    <td align="right">3.0523</td>
    <td align="right">22.82</td>
    <td align="right">21.53</td>
    <td align="right">24.67</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3118</td>
    <td align="right">89.90</td>
    <td align="right">80.43</td>
    <td align="right">44.04</td>
    <td align="center">5</td>
    <td align="right">1.0423</td>
    <td align="right">23.22</td>
    <td align="right">21.35</td>
    <td align="right">23.73</td>
    <td align="center">6</td>
    <td align="right">0.8142</td>
    <td align="right">25.06</td>
    <td align="right">22.32</td>
    <td align="right">24.66</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0453</td>
    <td align="right">110.62</td>
    <td align="right">100.85</td>
    <td align="right">44.53</td>
    <td align="center">6</td>
    <td align="right">0.3972</td>
    <td align="right">25.24</td>
    <td align="right">22.65</td>
    <td align="right">24.34</td>
    <td align="center">7</td>
    <td align="right">0.2784</td>
    <td align="right">27.61</td>
    <td align="right">24.17</td>
    <td align="right">25.50</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0062</td>
    <td align="right">139.99</td>
    <td align="right">125.64</td>
    <td align="right">45.26</td>
    <td align="center">7</td>
    <td align="right">0.1886</td>
    <td align="right">27.09</td>
    <td align="right">24.27</td>
    <td align="right">25.26</td>
    <td align="center">8</td>
    <td align="right">0.1259</td>
    <td align="right">30.15</td>
    <td align="right">25.52</td>
    <td align="right">26.29</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4144</td>
    <td align="right">22.93</td>
    <td align="right">41.28</td>
    <td align="right">41.36</td>
    <td align="center">5</td>
    <td align="right">2.3168</td>
    <td align="right">29.12</td>
    <td align="right">41.58</td>
    <td align="right">41.26</td>
    <td align="center">5</td>
    <td align="right">2.7253</td>
    <td align="right">18.72</td>
    <td align="right">25.48</td>
    <td align="right">25.51</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4200</td>
    <td align="right">27.87</td>
    <td align="right">56.23</td>
    <td align="right">56.88</td>
    <td align="center">8</td>
    <td align="right">0.3742</td>
    <td align="right">33.55</td>
    <td align="right">57.61</td>
    <td align="right">57.82</td>
    <td align="center">8</td>
    <td align="right">0.5350</td>
    <td align="right">17.52</td>
    <td align="right">36.17</td>
    <td align="right">25.58</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">40.46</td>
    <td align="right">76.71</td>
    <td align="right">76.67</td>
    <td align="center">11</td>
    <td align="right">0.0667</td>
    <td align="right">44.68</td>
    <td align="right">77.72</td>
    <td align="right">77.65</td>
    <td align="center">11</td>
    <td align="right">0.1194</td>
    <td align="right">28.96</td>
    <td align="right">55.00</td>
    <td align="right">39.54</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0150</td>
    <td align="right">43.99</td>
    <td align="right">86.10</td>
    <td align="right">86.22</td>
    <td align="center">14</td>
    <td align="right">0.0106</td>
    <td align="right">49.98</td>
    <td align="right">92.31</td>
    <td align="right">92.27</td>
    <td align="center">13</td>
    <td align="right">0.0276</td>
    <td align="right">29.18</td>
    <td align="right">55.74</td>
    <td align="right">40.24</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4823</td>
    <td align="right">18.66</td>
    <td align="right">26.03</td>
    <td align="right">26.16</td>
    <td align="center">5</td>
    <td align="right">2.4524</td>
    <td align="right">20.68</td>
    <td align="right">29.26</td>
    <td align="right">29.30</td>
    <td align="center">5</td>
    <td align="right">2.3084</td>
    <td align="right">20.92</td>
    <td align="right">30.75</td>
    <td align="right">30.80</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4562</td>
    <td align="right">18.95</td>
    <td align="right">46.37</td>
    <td align="right">35.29</td>
    <td align="center">8</td>
    <td align="right">0.4164</td>
    <td align="right">18.64</td>
    <td align="right">39.46</td>
    <td align="right">27.74</td>
    <td align="center">8</td>
    <td align="right">0.3847</td>
    <td align="right">21.04</td>
    <td align="right">51.88</td>
    <td align="right">40.26</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0862</td>
    <td align="right">28.75</td>
    <td align="right">54.42</td>
    <td align="right">38.68</td>
    <td align="center">11</td>
    <td align="right">0.0758</td>
    <td align="right">33.18</td>
    <td align="right">53.11</td>
    <td align="right">35.29</td>
    <td align="center">11</td>
    <td align="right">0.0626</td>
    <td align="right">32.14</td>
    <td align="right">61.35</td>
    <td align="right">43.65</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0188</td>
    <td align="right">28.75</td>
    <td align="right">55.49</td>
    <td align="right">39.50</td>
    <td align="center">13</td>
    <td align="right">0.0109</td>
    <td align="right">33.73</td>
    <td align="right">64.61</td>
    <td align="right">44.70</td>
    <td align="center">14</td>
    <td align="right">0.0103</td>
    <td align="right">33.62</td>
    <td align="right">64.02</td>
    <td align="right">44.54</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3219</td>
    <td align="right">25.06</td>
    <td align="right">42.89</td>
    <td align="right">35.03</td>
    <td align="center">6</td>
    <td align="right">2.2856</td>
    <td align="right">31.51</td>
    <td align="right">53.65</td>
    <td align="right">40.27</td>
    <td align="center">7</td>
    <td align="right">2.3420</td>
    <td align="right">37.38</td>
    <td align="right">59.67</td>
    <td align="right">60.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4140</td>
    <td align="right">35.29</td>
    <td align="right">60.21</td>
    <td align="right">35.48</td>
    <td align="center">7</td>
    <td align="right">0.3818</td>
    <td align="right">41.29</td>
    <td align="right">60.99</td>
    <td align="right">38.03</td>
    <td align="center">10</td>
    <td align="right">0.3419</td>
    <td align="right">45.33</td>
    <td align="right">77.35</td>
    <td align="right">77.13</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0858</td>
    <td align="right">40.82</td>
    <td align="right">73.98</td>
    <td align="right">35.82</td>
    <td align="center">10</td>
    <td align="right">0.0720</td>
    <td align="right">49.39</td>
    <td align="right">79.24</td>
    <td align="right">39.79</td>
    <td align="center">11</td>
    <td align="right">0.0511</td>
    <td align="right">48.64</td>
    <td align="right">83.34</td>
    <td align="right">83.56</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0216</td>
    <td align="right">52.54</td>
    <td align="right">93.73</td>
    <td align="right">37.37</td>
    <td align="center">12</td>
    <td align="right">0.0148</td>
    <td align="right">57.77</td>
    <td align="right">94.82</td>
    <td align="right">39.26</td>
    <td align="center">15</td>
    <td align="right">0.0066</td>
    <td align="right">67.04</td>
    <td align="right">118.36</td>
    <td align="right">118.54</td>
  </tr>
</table>

#### `N` = 10M elements
<table>
  <tr><th colspan="3"><code>boost::unordered_flat_set</code></tr>
  <tr>
    <th>insertion</th>
    <th>successful<br/>lookup</th>
    <th>unsuccessful<br/>lookup</th>
  </tr>
  <tr>
    <td align="right">71.36</td>
    <td align="right">38.44</td>
    <td align="right">12.20</td>
  </tr>
</table>
<table>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;K></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t,K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">6</td>
    <td align="right">2.1489</td>
    <td align="right">68.10</td>
    <td align="right">60.30</td>
    <td align="right">46.51</td>
    <td align="center">4</td>
    <td align="right">3.3441</td>
    <td align="right">23.70</td>
    <td align="right">21.31</td>
    <td align="right">26.15</td>
    <td align="center">5</td>
    <td align="right">3.0511</td>
    <td align="right">26.07</td>
    <td align="right">22.45</td>
    <td align="right">26.81</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">9</td>
    <td align="right">0.3184</td>
    <td align="right">115.03</td>
    <td align="right">91.19</td>
    <td align="right">49.61</td>
    <td align="center">5</td>
    <td align="right">1.0317</td>
    <td align="right">27.44</td>
    <td align="right">22.92</td>
    <td align="right">26.44</td>
    <td align="center">6</td>
    <td align="right">0.8206</td>
    <td align="right">31.74</td>
    <td align="right">26.63</td>
    <td align="right">28.44</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0455</td>
    <td align="right">144.35</td>
    <td align="right">124.39</td>
    <td align="right">51.65</td>
    <td align="center">6</td>
    <td align="right">0.4015</td>
    <td align="right">48.89</td>
    <td align="right">35.94</td>
    <td align="right">38.35</td>
    <td align="center">7</td>
    <td align="right">0.2865</td>
    <td align="right">43.12</td>
    <td align="right">28.32</td>
    <td align="right">32.48</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">14</td>
    <td align="right">0.0068</td>
    <td align="right">276.08</td>
    <td align="right">241.76</td>
    <td align="right">68.92</td>
    <td align="center">7</td>
    <td align="right">0.1883</td>
    <td align="right">36.88</td>
    <td align="right">32.43</td>
    <td align="right">31.38</td>
    <td align="center">8</td>
    <td align="right">0.1200</td>
    <td align="right">41.89</td>
    <td align="right">32.56</td>
    <td align="right">31.68</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t,K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4525</td>
    <td align="right">25.38</td>
    <td align="right">41.99</td>
    <td align="right">42.02</td>
    <td align="center">5</td>
    <td align="right">2.3280</td>
    <td align="right">31.74</td>
    <td align="right">42.29</td>
    <td align="right">41.84</td>
    <td align="center">5</td>
    <td align="right">2.7254</td>
    <td align="right">19.96</td>
    <td align="right">30.31</td>
    <td align="right">30.25</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4209</td>
    <td align="right">30.29</td>
    <td align="right">57.51</td>
    <td align="right">58.34</td>
    <td align="center">8</td>
    <td align="right">0.3751</td>
    <td align="right">37.15</td>
    <td align="right">60.53</td>
    <td align="right">60.28</td>
    <td align="center">8</td>
    <td align="right">0.5375</td>
    <td align="right">18.89</td>
    <td align="right">40.97</td>
    <td align="right">30.02</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0783</td>
    <td align="right">43.99</td>
    <td align="right">78.77</td>
    <td align="right">78.83</td>
    <td align="center">11</td>
    <td align="right">0.0645</td>
    <td align="right">48.90</td>
    <td align="right">81.10</td>
    <td align="right">80.57</td>
    <td align="center">11</td>
    <td align="right">0.1187</td>
    <td align="right">32.42</td>
    <td align="right">63.59</td>
    <td align="right">46.20</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0144</td>
    <td align="right">50.53</td>
    <td align="right">91.27</td>
    <td align="right">91.12</td>
    <td align="center">14</td>
    <td align="right">0.0117</td>
    <td align="right">59.47</td>
    <td align="right">97.86</td>
    <td align="right">97.76</td>
    <td align="center">13</td>
    <td align="right">0.0277</td>
    <td align="right">45.71</td>
    <td align="right">77.21</td>
    <td align="right">59.54</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock32&lt;K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>></code></th>
    <th colspan="5"><code>filter&lt;1,fast_multiblock64&lt;K>,1></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.4632</td>
    <td align="right">19.90</td>
    <td align="right">31.25</td>
    <td align="right">31.19</td>
    <td align="center">5</td>
    <td align="right">2.4414</td>
    <td align="right">21.91</td>
    <td align="right">33.69</td>
    <td align="right">33.42</td>
    <td align="center">5</td>
    <td align="right">2.3147</td>
    <td align="right">21.83</td>
    <td align="right">35.63</td>
    <td align="right">35.61</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">8</td>
    <td align="right">0.4402</td>
    <td align="right">20.02</td>
    <td align="right">51.10</td>
    <td align="right">39.99</td>
    <td align="center">8</td>
    <td align="right">0.4194</td>
    <td align="right">19.66</td>
    <td align="right">43.05</td>
    <td align="right">30.88</td>
    <td align="center">8</td>
    <td align="right">0.3773</td>
    <td align="right">22.19</td>
    <td align="right">56.73</td>
    <td align="right">45.55</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">11</td>
    <td align="right">0.0851</td>
    <td align="right">35.06</td>
    <td align="right">66.08</td>
    <td align="right">47.98</td>
    <td align="center">11</td>
    <td align="right">0.0779</td>
    <td align="right">34.76</td>
    <td align="right">58.63</td>
    <td align="right">40.09</td>
    <td align="center">11</td>
    <td align="right">0.0652</td>
    <td align="right">34.58</td>
    <td align="right">67.62</td>
    <td align="right">48.57</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">13</td>
    <td align="right">0.0183</td>
    <td align="right">40.59</td>
    <td align="right">76.99</td>
    <td align="right">56.31</td>
    <td align="center">13</td>
    <td align="right">0.0146</td>
    <td align="right">41.94</td>
    <td align="right">78.96</td>
    <td align="right">58.82</td>
    <td align="center">14</td>
    <td align="right">0.0112</td>
    <td align="right">39.97</td>
    <td align="right">78.05</td>
    <td align="right">56.35</td>
  </tr>
  <tr>
    <th></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>></code></th>
    <th colspan="5"><code>filter&lt;1,block&lt;uint64_t[8],K>,1></code></th>
    <th colspan="5"><code>filter&lt;1,multiblock&lt;uint64_t[8],K>></code></th>
  </tr>
  <tr>
    <th>c</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
    <th>K</th>
    <th>FPR<br/>[%]</th>
    <th>ins.</th>
    <th>succ.<br/>lkp.</th>
    <th>uns.<br/>lkp.</th>
  </tr>
  <tr>
    <td align="center">8</td>
    <td align="center">5</td>
    <td align="right">2.3203</td>
    <td align="right">27.60</td>
    <td align="right">43.56</td>
    <td align="right">38.37</td>
    <td align="center">6</td>
    <td align="right">2.2996</td>
    <td align="right">35.47</td>
    <td align="right">54.77</td>
    <td align="right">43.82</td>
    <td align="center">7</td>
    <td align="right">2.3251</td>
    <td align="right">40.69</td>
    <td align="right">60.83</td>
    <td align="right">61.05</td>
  </tr>
  <tr>
    <td align="center">12</td>
    <td align="center">7</td>
    <td align="right">0.4161</td>
    <td align="right">39.15</td>
    <td align="right">62.04</td>
    <td align="right">38.09</td>
    <td align="center">7</td>
    <td align="right">0.3865</td>
    <td align="right">47.20</td>
    <td align="right">63.61</td>
    <td align="right">40.66</td>
    <td align="center">10</td>
    <td align="right">0.3470</td>
    <td align="right">48.55</td>
    <td align="right">78.23</td>
    <td align="right">78.28</td>
  </tr>
  <tr>
    <td align="center">16</td>
    <td align="center">9</td>
    <td align="right">0.0852</td>
    <td align="right">46.78</td>
    <td align="right">78.93</td>
    <td align="right">41.40</td>
    <td align="center">10</td>
    <td align="right">0.0713</td>
    <td align="right">59.13</td>
    <td align="right">88.06</td>
    <td align="right">44.42</td>
    <td align="center">11</td>
    <td align="right">0.0480</td>
    <td align="right">52.72</td>
    <td align="right">86.11</td>
    <td align="right">85.87</td>
  </tr>
  <tr>
    <td align="center">20</td>
    <td align="center">12</td>
    <td align="right">0.0196</td>
    <td align="right">62.18</td>
    <td align="right">107.70</td>
    <td align="right">43.90</td>
    <td align="center">12</td>
    <td align="right">0.0155</td>
    <td align="right">77.43</td>
    <td align="right">113.54</td>
    <td align="right">50.40</td>
    <td align="center">15</td>
    <td align="right">0.0075</td>
    <td align="right">78.86</td>
    <td align="right">128.03</td>
    <td align="right">127.92</td>
  </tr>
</table>

<!--vs-x86/comparison_table.cpp.txt-->
